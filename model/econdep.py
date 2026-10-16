import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from model5 import *
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
m=np.median; q=lambda x,p: np.percentile(x,p)
def carry_econ(v,path,delta):
    """silicon on declining balance at rate delta (economic obsolescence); shell unchanged; same energization/deferral logic"""
    capex={**HIST,**PATHS[path]}
    ai={y:np.maximum(capex[y]-v['nonai']*(1+v['gn'])**(y-2023),0) for y in YEARS}
    defer=np.zeros(N); aiE={}; aiD={}
    for y in YEARS:
        tot=ai[y]+defer; e=np.minimum(tot,v['gridcap'])*(1-v['fdelay']) if y>=2026 else np.minimum(tot,v['gridcap']); aiE[y]=e; aiD[y]=tot-e; defer=tot-e
    H={}
    for t in TY:
        dep=np.zeros(N); gross=np.zeros(N); net=np.zeros(N)
        for c in YEARS:
            if c>t: continue
            age=t-c+0.5
            # silicon: declining balance
            f=v['lagsi'] if c==t else 1.0; G=aiE[c]*f*v['phi']
            nbv_start=G*(1-delta)**max(age-0.5,0); dep+=nbv_start*delta*(1 if age>=0.5 else 0.5); gross+=np.where(nbv_start>0.02*G,G,0); net+=nbv_start*(1-delta/2)
            # shell: straight line as before
            f=v['lagsh'] if c==t else 1.0; G=aiE[c]*f*(1-v['phi'])*v['ksite']; alive=age<v['Lsh']
            dep+=np.where(alive,G/v['Lsh'],0); gross+=np.where(alive,G,0); net+=np.where(alive,G*np.maximum(1-age/v['Lsh'],0),0)
        H[t]=dep+v['copex']*(1+v['pue_up'])*gross+v['r']*net+v['r']*aiD.get(t,0)
    return H
rng=np.random.default_rng(11); v=draw(rng); Hsl=carry(v,'Plateau'); end,rec,per=bottom_up(rng)
yrs=list(range(2027,2031)); print("straight-line H:",[f"{m(Hsl[t]):.0f}" for t in yrs])
fig,ax=plt.subplots(1,2,figsize=(11,3.5))
ax[0].plot(yrs,[m(Hsl[t]) for t in yrs],'k-',marker='o',label='Straight-line, effective life 4.2 yr (base)')
res={}
for d,ls in zip([0.5,0.7,0.9],[':','--','-.']):
    He=carry_econ(v,'Plateau',d); res[d]=He
    print(f"delta={d}: H",[f"{m(He[t]):.0f}" for t in yrs],"delta_t",[f"{m(rec[t]-v['circ']-He[t]):+.0f}" for t in yrs])
    ax[0].plot(yrs,[m(He[t]) for t in yrs],ls,color='0.3',marker='s',ms=3,label=f'Declining balance, {d:.0%}/yr economic obsolescence')
ax[0].plot(yrs,[m(rec[t]-v['circ']) for t in yrs],'-',color='0.6',marker='^',ms=3,label='Infrastructure receipts (bottom-up)')
ax[0].set_ylabel('$B/yr'); ax[0].set_xticks(yrs); ax[0].legend(fontsize=6.5); ax[0].set_title('Carry under accounting-style vs economic depreciation (Plateau)',fontsize=9)
# commodity floor: marginal cash cost per M tokens
rng2=np.random.default_rng(5); T_=lambda a,b,c: rng2.triangular(a,b,c,N)
kw=T_(0.7,0.9,1.2); pue=T_(1.12,1.22,1.35); tariff=T_(0.075,0.10,0.13); opex_hr=T_(0.05,0.10,0.18); util=T_(0.40,0.45,0.50)
cash_hr=kw*pue*tariff+opex_hr                       # $ per accelerator-hour
tok_hr=T_(3,6,10)*1e6*(util/0.45)                    # tokens per accelerator-hour at modeled utilization
mcc=cash_hr/tok_hr*1e6                               # $ per million tokens
mcc2=cash_hr/(tok_hr*2)*1e6                          # if utilization doubles
print("marginal cash cost $/Mtok med",round(m(mcc),3),"P10-P90",round(q(mcc,10),3),round(q(mcc,90),3),"| at 2x utilization",round(m(mcc2),3))
price=T_(0.10,0.30,1.0)  # blended realized $/Mtok, small-to-mid models weighted
print("price/floor ratio med",round(m(price/mcc),1))
ax[1].hist(mcc,bins=80,color='0.4',alpha=0.8,label='Marginal cash cost, current utilization'); ax[1].hist(mcc2,bins=80,color='0.75',alpha=0.8,label='...if utilization doubles')
for p_,lab in [(0.10,'small-model API ~$0.10'),(0.30,'blended ~$0.30'),(1.0,'mid-frontier ~$1.0')]: ax[1].axvline(p_,color='k',ls=':',lw=0.8); ax[1].text(p_,ax[1].get_ylim()[1]*0.9,lab,rotation=90,fontsize=6.5,va='top',ha='right')
ax[1].set_xscale('log'); ax[1].set_xlabel('$ per million tokens (log scale)'); ax[1].set_yticks([]); ax[1].legend(fontsize=6.5,loc='upper left'); ax[1].set_title('The commodity floor: marginal cash cost of inference vs realized prices',fontsize=9)
plt.tight_layout(); plt.savefig('f23_econdep_floor.pdf'); print('fig done')
# receipts at the floor: opex + tiny margin
opex_only=[m(v['copex']*(1+v['pue_up'])*0+0) for t in yrs]
