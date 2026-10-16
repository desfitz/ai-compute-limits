import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from model5 import *
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
m=np.median
# f16: distribution overlap by year, plateau
r=run('Plateau'); fig,axs=plt.subplots(1,4,figsize=(11,2.9),sharey=True)
for ax,t in zip(axs,TY):
    H=r['H'][t]; R=r['rec'][t]-r['circ']; pp=(R>H).mean()*100
    bins=np.linspace(min(R.min(),H.min()),max(R.max(),H.max()),70)
    ax.hist(H,bins=bins,color='0.25',alpha=0.8,label='Carry H_t'); ax.hist(R,bins=bins,color='0.65',alpha=0.8,label='Receipts')
    ax.set_title(f'{t}: P(receipts > carry) = {pp:.0f}%',fontsize=9); ax.set_xlabel('$B/yr'); ax.set_yticks([])
axs[0].legend(fontsize=7); fig.suptitle('Do the distributions overlap? Bottom-up receipts vs carry, Plateau',fontsize=9); plt.tight_layout(); plt.savefig('f16_overlap.pdf')
# P(profit) table by path/year/sov
print("P(profit) by path/year:")
for p in PATHS:
    for kap,gam,lab in [(1.0,0.0,'none'),(1.2,0.25,'sov')]:
        rr=run(p,kap,gam); print(p,lab,[f"{((rr['rec'][t]-rr['circ']-rr['H'][t])>0).mean()*100:.0f}%" for t in TY])
# f17: probability map P(delta_2030>0) over residual factor x copilot ceiling, with feasibility cutoffs
def pmap(path,mcap,copC):
    rng=np.random.default_rng(11); v=draw(rng); H=carry(v,path)
    old=SECTORS['Office assistants/agents']['C']; SECTORS['Office assistants/agents']['C']=(copC*0.8,copC,copC*1.2)
    end,rec,per=bottom_up(rng); SECTORS['Office assistants/agents']['C']=old
    d=rec[2030]*mcap-v['circ']-H[2030]; return (d>0).mean()*100, m(end[2030])*mcap
ms=np.linspace(0.7,1.7,11); cs=np.linspace(80,400,9)
fig,axs=plt.subplots(1,3,figsize=(11,3.6))
for ax,p in zip(axs,PATHS):
    Z=np.zeros((len(cs),len(ms))); E=np.zeros_like(Z)
    for i,c in enumerate(cs):
        for j,mc in enumerate(ms): Z[i,j],E[i,j]=pmap(p,mc,c)
    cf=ax.contourf(ms,cs,Z,levels=[0,5,10,25,50,75,90,95,100],cmap='Greys'); 
    ax.contour(ms,cs,Z,levels=[50],colors='k',linewidths=1.5)
    ax.axhline(268,color='k',ls='--',lw=1); ax.text(0.72,275,'IT-budget cap on assistants (~$270B)',fontsize=7)
    # end-customer feasibility: total 2030 AI revenue > 8% of IT spend + ads + consumer caps (~$810B) shaded
    ax.contour(ms,cs,E,levels=[920,1310],colors='k',linestyles=':',linewidths=1.0); ax.contourf(ms,cs,E,levels=[920,1310],colors=['none'],hatches=['..'],alpha=0)
    ax.plot([1.0],[150],'ko'); ax.set_title(f'{p}: P(profit 2030), %',fontsize=9); ax.set_xlabel('Residual adoption/capability factor'); 
axs[0].set_ylabel('Office assistant/agent ceiling 2030 ($B)'); axs[0].text(1.02,95,'paper modes',fontsize=7)
plt.colorbar(cf,ax=axs,fraction=0.02,label='P(receipts > carry), %')
fig.suptitle('Probability of overlap across the two residual axes. Solid: 50%. Dashed: copilot IT-budget cap. Dotted/hatched: feasibility band, total 2030 AI revenue = $920B-$1,310B (P10-P90 of the budget cutoff)',fontsize=8)
plt.savefig('f17_probmap.pdf',bbox_inches='tight'); print("done")
