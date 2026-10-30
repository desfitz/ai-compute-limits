import numpy as np, matplotlib; matplotlib.use('Agg'); import figstyle; import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from model5 import *
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
m=np.median; q=lambda x,p: np.percentile(x,p)
# ---- f18 now drawn in colour by figs_flow.py
# ---- f19: 2027-2035 by four paths
fig,ax=plt.subplots(1,2,figsize=(11,3.6)); yrs=list(range(2027,2036))
res={}
for p,ls in zip(PATHS,['-','--',':']):
    r=run(p); d={t:r['rec'][t]-r['circ']-r['H'][t] for t in yrs}; res[p]=d
    ax[0].plot(yrs,[m(d[t]) for t in yrs],ls,color=figstyle.PC.get(p,'#1E2761'),marker='o',ms=3,label=p)
    ax[1].plot(yrs,[m(sum(d[y] for y in yrs if y<=t)) for t in yrs],ls,color=figstyle.PC.get(p,'#1E2761'),marker='o',ms=3,label=p)
ra=adaptive(); res['Adaptive']=ra['d']
ax[0].plot(yrs,[m(ra['d'][t]) for t in yrs],'-.',color='#C0504D',marker='s',ms=3,label='Adaptive (rational operator)')
ax[1].plot(yrs,[m(sum(ra['d'][y] for y in yrs if y<=t)) for t in yrs],'-.',color='#C0504D',marker='s',ms=3,label='Adaptive')
for a in ax: a.axhline(0,color='#1E2761',lw=0.8); a.set_xticks(yrs); a.legend(fontsize=7)
ax[0].set_ylabel('Annual delta ($B, median)'); ax[1].set_ylabel('Cumulative delta from 2027 ($B, median)')
fig.suptitle('Extending the horizon to 2035: annual and cumulative surplus/deficit by capex path',fontsize=9); plt.tight_layout(); plt.savefig('f19_horizon2035.pdf')
# ---- f20: adaptive capex path and carry vs receipts
fig,ax=plt.subplots(figsize=(6.4,3.4))
ax.plot(yrs,[m(ra['capex'][t]) for t in yrs],'k-',marker='o',label='Adaptive capex')
ax.plot(yrs,[m(ra['H'][t]) for t in yrs],'k--',marker='s',ms=3,label='Carry H_t')
ax.plot(yrs,[m(ra['rec'][t]-ra['circ']) for t in yrs],'-',color='#E08E45',marker='^',ms=3,label='Infrastructure receipts')
ax.set_xticks(yrs); ax.set_ylabel('$B/yr'); ax.legend(fontsize=7); ax.set_title('A rational operator: capex follows last year\'s receipts-to-carry ratio (damped, bounded $400B-$1.1T)',fontsize=8.5)
plt.tight_layout(); plt.savefig('f20_adaptive.pdf')
print("tables:")
for p in res:
    d=res[p]; print(p,[f"{m(d[t]):+.0f} ({(d[t]>0).mean()*100:.0f}%)" for t in yrs])
    print("  cum:",[f"{m(sum(d[y] for y in yrs if y<=t)):+.0f}" for t in yrs])
print("adaptive capex:",[f"{m(ra['capex'][t]):.0f}" for t in yrs]); print("adaptive H:",[f"{m(ra['H'][t]):.0f}" for t in yrs])
r=run('Plateau'); print("end-customer 2031-35:",[f"{m(r['end'][t]):.0f}" for t in range(2031,2036)],"receipts:",[f"{m(r['rec'][t]):.0f}" for t in range(2031,2036)],"H:",[f"{m(r['H'][t]):.0f}" for t in range(2031,2036)])
