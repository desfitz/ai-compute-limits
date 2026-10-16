import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from model5 import *
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
m=np.median; q=lambda x,p: np.percentile(x,p)
# ---- f18: where a customer dollar goes
fig,ax=plt.subplots(figsize=(10,4.6)); ax.axis('off')
def box(x,y,w,h,t,fc='0.92'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02',fc=fc,ec='k',lw=1)); ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=8.5)
def arrow(x1,y1,x2,y2,t='',dy=0.02):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=12,lw=1,color='k'))
    if t: ax.text((x1+x2)/2,(y1+y2)/2+dy,t,ha='center',fontsize=7.5)
box(0.02,0.35,0.20,0.30,'END CUSTOMERS\nenterprises, consumers, advertisers\n\npay end-customer revenue $D_t$\n(sum over sectors of $R_s$)',fc='0.85')
box(0.32,0.68,0.22,0.22,'FRONTIER LABS\nOpenAI, Anthropic, others\nkeep gross margin (1-$\\theta_{lab}$)\nbuy compute with the rest')
box(0.32,0.39,0.22,0.22,'HYPERSCALER AI SERVICES\nAzure AI, Bedrock, Vertex, seats\n$\\theta\\approx1$: same balance sheet')
box(0.32,0.10,0.22,0.22,'ADVERTISING and CONSUMER\nMeta, Google, subscriptions\n$\\theta\\approx1$ (ads), $\\approx0.85$ (subs)')
box(0.64,0.39,0.22,0.22,'INFRASTRUCTURE OWNERS\nBig-5 data centers\nreceive INFRASTRUCTURE RECEIPTS\n$=\\sum_s\\theta_s R_s$',fc='0.80')
box(0.64,0.05,0.22,0.20,'LEAKAGE (never reaches the meter)\non-device NPUs, on-premise clusters,\nintegrator margin, open-weight models',fc='1.0')
box(0.64,0.74,0.22,0.16,'INVESTOR CAPITAL\nlab equity rounds ($\\sim$\\$190B in 2026)\nbridging, not customer revenue',fc='1.0')
arrow(0.22,0.60,0.32,0.79,'lab channel ~50%'); arrow(0.22,0.50,0.32,0.50,'direct ~20%'); arrow(0.22,0.40,0.32,0.21,'ads+consumer ~30%')
arrow(0.54,0.79,0.64,0.55,'compute spend $\\theta_{lab}\\approx0.64$'); arrow(0.54,0.50,0.64,0.50); arrow(0.54,0.21,0.64,0.45)
arrow(0.64,0.80,0.66,0.61,'',0); arrow(0.22,0.38,0.64,0.15,'',0)
ax.text(0.75,0.34,'compared with CARRY $H_t$\n(depreciation + opex + return)',ha='center',fontsize=8.5,style='italic')
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_title('Where an AI customer dollar goes: end-customer revenue, cloud-capture share, infrastructure receipts',fontsize=9)
plt.tight_layout(); plt.savefig('f18_flow.pdf')
# ---- f19: 2027-2035 by four paths
fig,ax=plt.subplots(1,2,figsize=(11,3.6)); yrs=list(range(2027,2036))
res={}
for p,ls in zip(PATHS,['-','--',':']):
    r=run(p); d={t:r['rec'][t]-r['circ']-r['H'][t] for t in yrs}; res[p]=d
    ax[0].plot(yrs,[m(d[t]) for t in yrs],ls,color='k',marker='o',ms=3,label=p)
    ax[1].plot(yrs,[m(sum(d[y] for y in yrs if y<=t)) for t in yrs],ls,color='k',marker='o',ms=3,label=p)
ra=adaptive(); res['Adaptive']=ra['d']
ax[0].plot(yrs,[m(ra['d'][t]) for t in yrs],'-.',color='0.4',marker='s',ms=3,label='Adaptive (rational operator)')
ax[1].plot(yrs,[m(sum(ra['d'][y] for y in yrs if y<=t)) for t in yrs],'-.',color='0.4',marker='s',ms=3,label='Adaptive')
for a in ax: a.axhline(0,color='k',lw=0.8); a.set_xticks(yrs); a.legend(fontsize=7)
ax[0].set_ylabel('Annual delta ($B, median)'); ax[1].set_ylabel('Cumulative delta from 2027 ($B, median)')
fig.suptitle('Extending the horizon to 2035: annual and cumulative surplus/deficit by capex path',fontsize=9); plt.tight_layout(); plt.savefig('f19_horizon2035.pdf')
# ---- f20: adaptive capex path and carry vs receipts
fig,ax=plt.subplots(figsize=(6.4,3.4))
ax.plot(yrs,[m(ra['capex'][t]) for t in yrs],'k-',marker='o',label='Adaptive capex')
ax.plot(yrs,[m(ra['H'][t]) for t in yrs],'k--',marker='s',ms=3,label='Carry H_t')
ax.plot(yrs,[m(ra['rec'][t]-ra['circ']) for t in yrs],'-',color='0.5',marker='^',ms=3,label='Infrastructure receipts')
ax.set_xticks(yrs); ax.set_ylabel('$B/yr'); ax.legend(fontsize=7); ax.set_title('A rational operator: capex follows last year\'s receipts-to-carry ratio (damped, bounded $400B-$1.1T)',fontsize=8.5)
plt.tight_layout(); plt.savefig('f20_adaptive.pdf')
print("tables:")
for p in res:
    d=res[p]; print(p,[f"{m(d[t]):+.0f} ({(d[t]>0).mean()*100:.0f}%)" for t in yrs])
    print("  cum:",[f"{m(sum(d[y] for y in yrs if y<=t)):+.0f}" for t in yrs])
print("adaptive capex:",[f"{m(ra['capex'][t]):.0f}" for t in yrs]); print("adaptive H:",[f"{m(ra['H'][t]):.0f}" for t in yrs])
r=run('Plateau'); print("end-customer 2031-35:",[f"{m(r['end'][t]):.0f}" for t in range(2031,2036)],"receipts:",[f"{m(r['rec'][t]):.0f}" for t in range(2031,2036)],"H:",[f"{m(r['H'][t]):.0f}" for t in range(2031,2036)])
