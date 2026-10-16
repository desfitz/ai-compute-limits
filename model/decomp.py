import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from model5 import *
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
q=lambda x,p: np.percentile(x,p); m=np.median; sl=lambda x: np.std(np.log(x))
rng=np.random.default_rng(21)
# ---- A. 2026 revenue base decomposition (calendar-2026 booked, $B)
comp={'Anthropic booked (gross basis)':(50,57,65),'OpenAI booked':(26,29,33),'Other labs':(4,7,12),
      'Hyperscaler AI services ex-lab hosting':(25,35,45),'Advertising uplift (Meta+Google)':(25,40,55),
      'Consumer/search/internal not in labs':(8,15,25),'Overlap correction (reseller gross basis)':(-15,-8,0)}
parts={k:T(rng,*v) for k,v in comp.items()}; base=sum(parts.values())
print("BASE 2026: median",round(m(base)),"P10-P90",round(q(base,10)),round(q(base,90))," sigma_ln",round(sl(base),3)," vs old Triang(160,210,300) sigma_ln",round(sl(T(rng,160,210,300)),3))
for k,v in parts.items(): print(f"  {k:42s} {m(v):6.1f}  sigma_ln {sl(np.abs(v)+1e-9) if v.min()>0 else float('nan'):.3f}")
# ---- B. theta decomposition
th_lab=T(rng,0.50,0.65,0.85); th_direct=T(rng,0.9,1.0,1.0); th_ads=np.ones(N); th_cons=T(rng,0.75,0.85,0.95)
w_lab=(parts['Anthropic booked (gross basis)']+parts['OpenAI booked']+parts['Other labs']+parts['Overlap correction (reseller gross basis)'])/base
w_dir=parts['Hyperscaler AI services ex-lab hosting']/base; w_ads=parts['Advertising uplift (Meta+Google)']/base; w_cons=parts['Consumer/search/internal not in labs']/base
theta=w_lab*th_lab+w_dir*th_direct+w_ads*th_ads+w_cons*th_cons
print("THETA 2026: median",round(m(theta),3),"P10-P90",round(q(theta,10),3),round(q(theta,90),3)," sigma_ln",round(sl(theta),3)," vs old Triang(0.7,0.85,1.0) sigma_ln",round(sl(T(rng,0.7,0.85,1.0)),3))
# ---- C. ad ceiling decomposition 2030
meta30=T(rng,330,380,430); goog30=T(rng,380,450,520); lift=T(rng,0.08,0.12,0.18); native=T(rng,10,25,60)
adC=(meta30+goog30)*lift+native
print("AD CEILING 2030: median",round(m(adC)),"P10-P90",round(q(adC,10)),round(q(adC,90))," sigma_ln",round(sl(adC),3)," vs old Triang(80,150,250) sigma_ln",round(sl(T(rng,80,150,250)),3))
# ---- D. common factor decomposition
sIT,sPrice,sCap=0.05,0.08,0.10
print("COMMON FACTOR: sqrt(",sIT**2,"+",sPrice**2,"+",sCap**2,") =",round((sIT**2+sPrice**2+sCap**2)**0.5,3)," (target 0.14)")
# ---- E. re-run top-down variance budget with decomposed base & theta
newD0=(q(base,2),m(base),q(base,98)); newTh=(q(theta,2),m(theta),q(theta,98))
print("new D0 triang",[round(x) for x in newD0]," new theta",[round(x,3) for x in newTh])
basep=dict(nonai=(140,165,200),phi=(0.45,0.55,0.65),Lsi=(3,4,5.5),Lsh=(15,20,25),copex=(0.059,0.0665,0.074),r=(0.09,0.105,0.12),lag=(0.3,0.5,0.7),D0=newD0,theta=newTh)
modes={k:(v[1],v[1],v[1]+1e-4) for k,v in basep.items()}
def td(over,g=0.42): o=topdown('Plateau',g,over=over)[2030]; return m(o['D']-o['H'])
d0=td(modes); half={}
for k,(a,b,c) in basep.items():
    lo=dict(modes);lo[k]=(a,a,a+1e-4); hi=dict(modes);hi[k]=(c,c,c+1e-4); half[k]=abs(td(hi)-td(lo))/2
tot=sum(v*v for v in half.values()); print("Top-down variance budget AFTER decomposition (g=42%, base delta",round(d0),"):")
for k,v in sorted(half.items(),key=lambda x:-x[1]): print(f"  {k:6s} half {v:5.0f} share {v*v/tot*100:4.1f}%")
print("  RSS",round(tot**0.5))
# ---- F. bottom-up with decomposed ad ceiling & theta_lab: what-if curves
SECTORS['Advertising uplift']['C']=(q(adC,5),m(adC),q(adC,95))
def bu_delta(path,mcap=1.0,adC=None,copC=None,thlab=None,seed=11):
    rng=np.random.default_rng(seed); v=draw(rng); H=carry(v,path)
    if adC: SECTORS['Advertising uplift']['C']=adC
    if copC: SECTORS['Office copilots/agents']['C']=copC
    end,rec,per=bottom_up(rng)
    if thlab is not None:  # scale lab-channel-heavy sectors' receipts? approximate: scale receipts by thlab/0.65 on 50% of receipts
        rec={t:rec[t]*(0.5+0.5*thlab/0.65) for t in rec}
    d=rec[2030]*mcap-v['circ']-H[2030]; return d
# f13: z and P(deficit) vs residual capability factor
fig,ax=plt.subplots(1,2,figsize=(10,3.4)); ms=np.arange(0.6,1.61,0.1)
for p,ls in zip(PATHS,['-','--',':']):
    z=[];pl=[]
    for mc in ms: d=bu_delta(p,mcap=mc); z.append(m(d)/np.std(d)); pl.append((d<0).mean()*100)
    ax[0].plot(ms,z,ls,color='k',marker='o',ms=3,label=p); ax[1].plot(ms,pl,ls,color='k',marker='o',ms=3,label=p)
ax[0].axhline(0,color='gray',lw=0.8); ax[0].axhline(-2,color='gray',lw=0.6,ls=':'); ax[0].axhline(2,color='gray',lw=0.6,ls=':')
ax[0].set_xlabel('Residual adoption/capability factor on 2030 receipts'); ax[0].set_ylabel('z = delta_2030 / sigma'); ax[0].legend(fontsize=7)
ax[1].set_xlabel('Residual adoption/capability factor on 2030 receipts'); ax[1].set_ylabel('P(deficit 2030), %'); ax[1].legend(fontsize=7)
fig.suptitle('What-if 1: the residual factor no decomposition removes',fontsize=9); plt.tight_layout(); plt.savefig('f13_whatif_mcap.pdf')
# f14: contour ad ceiling x copilot ceiling
ads=np.linspace(80,300,12); cops=np.linspace(120,400,12); Z=np.zeros((len(cops),len(ads)))
for i,c in enumerate(cops):
    for j,a in enumerate(ads):
        Z[i,j]=m(bu_delta('Plateau',adC=(a*0.8,a,a*1.2),copC=(c*0.8,c,c*1.2)))
SECTORS['Advertising uplift']['C']=(q(adC,5),m(adC),q(adC,95)); SECTORS['Office copilots/agents']['C']=(100,150,230)
fig,ax=plt.subplots(figsize=(6.2,4.2)); cs=ax.contourf(ads,cops,Z,levels=12,cmap='Greys_r'); plt.colorbar(cs,label='median delta_2030 ($B), Plateau')
ax.plot([m(adC)],[150],'ko'); ax.annotate('paper modes',(m(adC),150),xytext=(8,8),textcoords='offset points',fontsize=8)
ax.set_xlabel('Advertising uplift ceiling 2030 ($B)'); ax.set_ylabel('Office copilots/agents ceiling 2030 ($B)'); ax.set_title('What-if 2: the two largest ceilings; no break-even in range',fontsize=9)
plt.tight_layout(); plt.savefig('f14_whatif_ceilings.pdf')
# f15: z vs theta_lab and vs 2026 base
fig,ax=plt.subplots(1,2,figsize=(10,3.4)); ths=np.arange(0.45,0.96,0.05)
for p,ls in zip(PATHS,['-','--',':']):
    ax[0].plot(ths,[m(bu_delta(p,thlab=t)) for t in ths],ls,color='k',marker='o',ms=3,label=p)
ax[0].axhline(0,color='gray',lw=0.8); ax[0].set_xlabel('Lab-channel infrastructure share (compute cost / lab revenue)'); ax[0].set_ylabel('median delta_2030 ($B)'); ax[0].legend(fontsize=7)
bs=np.arange(150,301,15)
for p,ls in zip(PATHS,['-','--',':']):
    zz=[]
    for b in bs:
        o=topdown(p,0.49,over=dict(D0=(b*0.9,b,b*1.1)))[2030]; d=o['D']-o['H']; zz.append(m(d))
    ax[1].plot(bs,zz,ls,color='k',marker='o',ms=3,label=p)
ax[1].axhline(0,color='gray',lw=0.8); ax[1].set_xlabel('Calendar-2026 AI revenue base ($B), top-down at g=42%'); ax[1].set_ylabel('median delta_2030 ($B)'); ax[1].legend(fontsize=7)
fig.suptitle('What-if 3: lab economics and the 2026 base',fontsize=9); plt.tight_layout(); plt.savefig('f15_whatif_theta_base.pdf')
# final bottom-up with decomposed inputs
r=run('Plateau'); d=r['rec'][2030]-r['circ']-r['H'][2030]
print("BOTTOM-UP 2030 with decomposed ad ceiling: delta med",round(m(d)),"sd",round(np.std(d)),"z",round(m(d)/np.std(d),2),"P<0",round((d<0).mean(),3)," end2030",round(m(r['end'][2030])))
