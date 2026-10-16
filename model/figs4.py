import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, pandas as pd
from model5 import *
from model5 import topdown as _td
def simulate(path,g,seed=7,over=None):
    o=_td(path,g,seed,over); return {t:dict(H=o[t]["H"],D=o[t]["D"],d=o[t]["D"]-o[t]["H"]) for t in o}
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
q=lambda x,p: np.percentile(x,p)
# F1 capex history + AI attributable
d=pd.read_csv('epoch_capex.csv'); d['Y']=d['Calendar Quarter'].str[2:6].astype(int)
cols=['MSFT','AMZN','GOOG','META','ORCL']; ann=d.groupby('Y')[[c+' Broad CapEx ($M)' for c in cols]].sum()/1000
fig,ax=plt.subplots(figsize=(6.2,3.2)); bottom=np.zeros(len(ann)+1); yrs=list(ann.index)+[2026]
guid={'AMZN':200,'MSFT':190,'GOOG':180,'META':130,'ORCL':45}
for c in cols:
    vals=list(ann[c+' Broad CapEx ($M)'])+[guid[c]]; ax.bar(yrs,vals,bottom=bottom,label=c); bottom+=vals
ax.axhline(165,color='k',ls='--',lw=1); ax.text(2022.6,175,'2022 pre-AI baseline (~$165B)',fontsize=8)
ax.set_ylabel('Big-5 capex ($B/yr)'); ax.legend(ncol=5,fontsize=7,loc='upper left'); ax.set_xticks(yrs)
ax.set_title('Capex: Epoch AI (SEC XBRL, 2022-25) and 2026 guidance',fontsize=9)
plt.tight_layout(); plt.savefig('f1_capex.pdf')
# F2 carry ramp
fig,ax=plt.subplots(figsize=(6.2,3.2)); yrs=range(2027,2031)
for p,ls in zip(PATHS,['-','--',':']):
    o=simulate(p,0.3); med=[np.median(o[t]['H']) for t in yrs]
    ax.plot(yrs,med,ls,color='k',marker='o',label=p)
    if p=='Plateau': ax.fill_between(yrs,[q(o[t]['H'],10) for t in yrs],[q(o[t]['H'],90) for t in yrs],color='gray',alpha=0.25,label='Plateau P10-P90')
ax.set_ylabel('Annual carry H_t ($B)'); ax.set_xticks(list(yrs)); ax.legend(); ax.set_ylim(0,1200)
ax.set_title('Carry cost of the AI-attributable installed base',fontsize=9)
plt.tight_layout(); plt.savefig('f2_carry.pdf')
# F3 scissors
fig,ax=plt.subplots(figsize=(6.2,3.4)); o=simulate('Plateau',0.3)
ax.plot(yrs,[np.median(o[t]['H']) for t in yrs],'k-',lw=2.2,marker='o',label='Carry H_t (Plateau)')
ax.fill_between(yrs,[q(o[t]['H'],10) for t in yrs],[q(o[t]['H'],90) for t in yrs],color='gray',alpha=0.25)
for g,ls in zip([0.2,0.35,0.5,0.7],[':','-.','--','-']):
    o=simulate('Plateau',g); ax.plot(yrs,[np.median(o[t]['D']) for t in yrs],ls,color='0.35',marker='s',ms=3,label=f'Infra receipts at g={g:.0%}')
ax.set_ylabel('$B/yr'); ax.set_xticks(list(yrs)); ax.legend(fontsize=7); ax.set_ylim(0,1400)
ax.set_title('The scissors: carry versus infrastructure receipts by growth rate',fontsize=9)
plt.tight_layout(); plt.savefig('f3_scissors.pdf')
# F4 delta by year
fig,ax=plt.subplots(figsize=(6.2,3.2))
for g,ls in zip([0.2,0.3,0.4,0.5,0.6,0.8],[':','-.','--','-','-','-']):
    o=simulate('Plateau',g); ax.plot(yrs,[np.median(o[t]['d']) for t in yrs],ls,marker='o',ms=3,label=f'g={g:.0%}')
ax.axhline(0,color='k',lw=0.8); ax.set_ylabel('Median delta_t ($B)'); ax.set_xticks(list(yrs)); ax.legend(ncol=3,fontsize=7)
ax.set_title('Annual surplus/deficit by sustained growth rate (Plateau)',fontsize=9)
plt.tight_layout(); plt.savefig('f4_delta.pdf')
# F5 breakeven
fig,ax=plt.subplots(figsize=(6.2,3.2))
for p,ls in zip(PATHS,['-','--',':']):
    ax.plot(list(yrs),[min(breakeven(p,t),1.5)*100 for t in yrs],ls,color='k',marker='o',label=p)
for lab,ov,c in [('Plateau, D2026=$158B',dict(D0=(158,158,158.0001)),'0.6'),('Plateau, D2026=$197B',dict(D0=(197,197,197.0001)),'0.6')]:
    ax.plot(list(yrs),[min(breakeven('Plateau',t,ov),1.5)*100 for t in yrs],'-',color=c,marker='^',ms=3,label=lab)
ax.set_ylabel('Break-even sustained g* (%/yr)'); ax.set_xticks(list(yrs)); ax.legend(fontsize=7); ax.set_ylim(0,150)
ax.set_title('Growth rate at which the installed base earns its carry',fontsize=9)
plt.tight_layout(); plt.savefig('f5_breakeven.pdf')
# F6 cumulative
fig,ax=plt.subplots(figsize=(6.2,3.2)); gs=np.arange(0.1,1.01,0.05)
for p,ls in zip(PATHS,['-','--',':']):
    cum=[];lo=[];hi=[]
    for g in gs:
        o=simulate(p,g); c=sum(o[t]['d'] for t in yrs); cum.append(np.median(c)); lo.append(q(c,10)); hi.append(q(c,90))
    ax.plot(gs*100,cum,ls,color='k',label=p)
    if p=='Plateau': ax.fill_between(gs*100,lo,hi,color='gray',alpha=0.25)
ax.axhline(0,color='k',lw=0.8); ax.set_xlabel('Sustained growth g (%/yr)'); ax.set_ylabel('Cumulative delta 2027-30 ($B)'); ax.legend()
ax.set_title('Cumulative surplus/deficit versus growth',fontsize=9)
plt.tight_layout(); plt.savefig('f6_cum.pdf')
# F7 tornado on delta_2030 at g=49% plateau
base=dict(ai23=(20,30,40),gn=(0.02,0.06,0.10),phi=(0.45,0.52,0.60),gridcap=(1150,1400,1680),fdelay=(0.10,0.20,0.35),ksite=(1.02,1.05,1.09),pue_up=(0.00,0.03,0.06),ftrain=(0.35,0.45,0.55),Ltr=(2.5,3.5,4.5),Linf=(4.0,5.0,6.0),Lsh=(15,20,25),copex=(0.059,0.0665,0.074),r=(0.090,0.0945,0.099),lagsi=(0.5,0.7,0.9),lagsh=(0.2,0.4,0.6),D0=(163,179,194),theta=(0.77,0.815,0.86))
modes={k:(v[1],v[1],v[1]+1e-4) for k,v in base.items()}
d0=np.median(simulate('Plateau',0.49,over=modes)[2030]['d'])
rows=[]
for k,(a,b,c) in base.items():
    lo=dict(modes); lo[k]=(a,a,a+1e-4); hi=dict(modes); hi[k]=(c,c,c+1e-4)
    dl=np.median(simulate('Plateau',0.49,over=lo)[2030]['d']); dh=np.median(simulate('Plateau',0.49,over=hi)[2030]['d'])
    rows.append((k,dl,dh))
rows.sort(key=lambda r:abs(r[2]-r[1]))
names={'ai23':'AI capex in 2023 (sets baseline)','gridcap':'Grid energization cap','fdelay':'Siting/consent deferral','ksite':'Site cost uplift (water, consent)','pue_up':'Cooling opex uplift (water)','gn':'Non-AI baseline growth','phi':'Silicon share','ftrain':'Training share of fleet','Ltr':'Training-cluster life','Linf':'Inference-fleet life','Lsh':'Shell life','copex':'Facility opex','r':'Cost of capital','lagsi':'Silicon energization lag','lagsh':'Shell energization lag','D0':'2026 AI revenue base','theta':'Infra share of revenue'}
fig,ax=plt.subplots(figsize=(6.2,3.4))
for i,(k,dl,dh) in enumerate(rows):
    ax.barh(i,dh-d0,left=d0,color='0.3'); ax.barh(i,dl-d0,left=d0,color='0.7')
ax.set_yticks(range(len(rows))); ax.set_yticklabels([names[r[0]] for r in rows]); ax.axvline(d0,color='k',lw=0.8)
ax.set_xlabel('Median delta_2030 ($B), Plateau, g=49%. Dark: parameter at max; light: at min')
ax.set_title(f'One-at-a-time sensitivity (base delta_2030 = {d0:+.0f})',fontsize=9)
plt.tight_layout(); plt.savefig('f7_tornado.pdf')
print("tornado rows",[(k,round(dl),round(dh)) for k,dl,dh in rows],"base",round(d0))
# F8 histogram
fig,ax=plt.subplots(figsize=(6.2,3.0)); o=simulate('Plateau',0.49)[2030]['d']
ax.hist(o,bins=80,color='0.5'); ax.axvline(0,color='k'); ax.set_xlabel('delta_2030 ($B), Plateau, g=49%'); ax.set_ylabel('count')
ax.set_title(f'Distribution of the 2030 outcome: P(deficit) = {(o<0).mean()*100:.0f}%',fontsize=9)
plt.tight_layout(); plt.savefig('f8_hist.pdf'); print("done")
