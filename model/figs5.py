import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from model5 import *
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
q=lambda x,p: np.percentile(x,p); m=np.median
r=run('Plateau'); yrs=list(range(2026,2031))
# F9 stacked sectors (end-customer)
fig,ax=plt.subplots(figsize=(6.4,3.6)); bottom=np.zeros(5)
order=sorted(SECTORS,key=lambda s:-m(r['per'][s][2030]))
cm=plt.get_cmap('tab20')
for i,s in enumerate(order):
    v=[m(r['per'][s][t]) for t in yrs]; ax.bar(yrs,v,bottom=bottom,label=s,color=cm(i%20)); bottom+=v
ax.set_ylabel('End-customer AI revenue ($B/yr, median)'); ax.legend(fontsize=6,ncol=3,loc='upper left'); ax.set_xticks(yrs); ax.set_ylim(0,1000)
ax.set_title('Bottom-up demand by sector (logistic ramps to sector ceilings)',fontsize=9)
plt.tight_layout(); plt.savefig('f9_sectors.pdf')
# F10 three-way
fig,ax=plt.subplots(figsize=(6.4,3.6)); ty=list(TY)
ax.plot(ty,[m(r['H'][t]) for t in ty],'k-',lw=2.2,marker='o',label='Carry H_t (Plateau)')
ax.fill_between(ty,[q(r['H'][t],10) for t in ty],[q(r['H'][t],90) for t in ty],color='gray',alpha=0.25)
ax.plot(ty,[m(r['rec'][t]) for t in ty],'-',color='0.3',marker='s',label='Bottom-up cloud receipts')
ax.fill_between(ty,[q(r['rec'][t],10) for t in ty],[q(r['rec'][t],90) for t in ty],color='0.3',alpha=0.2)
ax.plot(ty,[m(r['end'][t]) for t in ty],'--',color='0.3',marker='s',ms=3,label='Bottom-up end-customer revenue')
o=topdown('Plateau',0.49); ax.plot(ty,[m(o[t]['D']) for t in ty],':',color='k',marker='^',ms=3,label='Top-down receipts at g*=49%')
ax.set_ylabel('$B/yr'); ax.set_xticks(ty); ax.legend(fontsize=7); ax.set_ylim(0,1000)
ax.set_title('Reconciliation: carry vs bottom-up demand vs top-down break-even path',fontsize=9)
plt.tight_layout(); plt.savefig('f10_reconcile.pdf')
# F11 sector tornado: delta_2030 sensitivity to each sector ceiling at min/max
base=m(r['rec'][2030]-r['circ']-r['H'][2030])
rows=[]
for s in SECTORS:
    for which,idx in (('lo',0),('hi',2)):
        old=SECTORS[s]['C']; SECTORS[s]['C']=(old[idx],old[idx],old[idx]+1e-4)
        rr=run('Plateau'); d=m(rr['rec'][2030]-rr['circ']-rr['H'][2030]); SECTORS[s]['C']=old
        rows.append((s,which,d))
lo={s:d for s,w,d in rows if w=='lo'}; hi={s:d for s,w,d in rows if w=='hi'}
ss=sorted(SECTORS,key=lambda s:abs(hi[s]-lo[s]))
fig,ax=plt.subplots(figsize=(6.4,4.0))
for i,s in enumerate(ss):
    ax.barh(i,hi[s]-base,left=base,color='0.3'); ax.barh(i,lo[s]-base,left=base,color='0.7')
ax.set_yticks(range(len(ss))); ax.set_yticklabels(ss,fontsize=7); ax.axvline(base,color='k',lw=0.8)
ax.set_xlabel('Median delta_2030 ($B), Plateau. Dark: sector ceiling at max; light: at min'); ax.set_title(f'Which sector ceilings matter (base delta_2030 = {base:+.0f})',fontsize=9)
plt.tight_layout(); plt.savefig('f11_sector_tornado.pdf')
print("base",round(base),[(s,round(lo[s]),round(hi[s])) for s in ss[-5:]])
# F12 growth decay: bottom-up implied g by year vs g* by year
fig,ax=plt.subplots(figsize=(6.4,3.2))
e=r['end']; ax.plot(ty,[100*(m(e[t]/e[t-1])-1) for t in ty],'-',color='0.3',marker='s',label='Bottom-up implied growth (yr/yr)')
for p,ls in zip(PATHS,['-','--',':']): ax.plot(ty,[min(breakeven(p,t),1.5)*100 for t in ty],ls,color='k',marker='o',label=f'Break-even sustained g* ({p})')
ax.set_ylabel('%/yr'); ax.set_xticks(ty); ax.legend(fontsize=7); ax.set_ylim(0,150)
ax.set_title('Growth the sectors deliver versus growth the stock requires',fontsize=9)
plt.tight_layout(); plt.savefig('f12_growth.pdf'); print('done')
