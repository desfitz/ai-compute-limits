import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':8.5,'axes.spines.top':False,'axes.spines.right':False})
N=100_000; rng=np.random.default_rng(9); T=lambda a,b,c: rng.triangular(a,b,c,N); m=np.median; q=lambda x,p: np.percentile(x,p)
H=8760
# producer tiers: (label, kW, PUE, tariff $/kWh, opex $/hr, capex per accelerator-slot all-in $k, life yr, util, tokens/hr M, cost of capital, capacity share 2030)
tiers=[
 ('In-house silicon, US (TPU/Trainium/MTIA)',(0.6,0.8,1.0),(1.1,1.2,1.3),(0.07,0.09,0.12),(0.05,0.08,0.12),(20,28,38),(3.5,4.5,5.5),(0.40,0.50,0.60),(4,7,11),(0.09,0.095,0.10),0.30),
 ('Nvidia-based hyperscaler, US',(0.7,0.9,1.2),(1.12,1.22,1.35),(0.075,0.10,0.13),(0.05,0.10,0.18),(35,45,55),(3.0,4.0,5.0),(0.35,0.45,0.55),(3,6,10),(0.09,0.095,0.10),0.35),
 ('Neo-cloud (leased, debt-funded)',(0.7,0.9,1.2),(1.2,1.3,1.45),(0.08,0.11,0.14),(0.08,0.14,0.22),(38,48,60),(2.5,3.5,4.5),(0.30,0.40,0.55),(3,6,10),(0.11,0.13,0.16),0.12),
 ('China western corridor (domestic silicon)',(0.9,1.3,1.8),(1.15,1.3,1.5),(0.02,0.03,0.045),(0.03,0.05,0.08),(18,28,40),(3.0,4.0,5.0),(0.40,0.55,0.70),(1.5,3,5),(0.04,0.06,0.08),0.13),
 ('On-premise open-weight, routine (small models)',(0.3,0.45,0.7),(1.3,1.5,1.8),(0.08,0.11,0.15),(0.03,0.06,0.10),(8,15,25),(4,5,6),(0.15,0.25,0.40),(15,30,60),(0.08,0.10,0.12),0.10),
]
rows=[]
for lab,kw,pue,tar,opx,cap,life,util,tok,r,share in tiers:
    kW=T(*kw); PUE=T(*pue); tf=T(*tar); ox=T(*opx); K=T(*cap)*1000; L=T(*life); u=T(*util); tk=T(*tok)*1e6; rr=T(*r)
    cash_hr=kW*PUE*tf+ox; tok_hr=tk*(u/0.45)
    carry_hr=K*(1/L+rr*0.6)/(H)   # depreciation + return on ~60% avg net book, per calendar hour
    mcc=cash_hr/tok_hr*1e6; full=(cash_hr+carry_hr)/tok_hr*1e6
    rows.append((lab,m(mcc),q(mcc,10),q(mcc,90),m(full),q(full,10),q(full,90),share))
    print(f"{lab:48s} cash {m(mcc):.3f} ({q(mcc,10):.3f}-{q(mcc,90):.3f})  full {m(full):.2f} ({q(full,10):.2f}-{q(full,90):.2f}) $/Mtok")
rows.sort(key=lambda x:x[4])
fig,ax=plt.subplots(figsize=(10,4)); x=0
for lab,mc,mlo,mhi,fc,flo,fhi,sh in rows:
    w=sh*100
    ax.bar(x+w/2,fc,width=w,color='0.75',edgecolor='k',lw=0.6); ax.bar(x+w/2,mc,width=w,color='0.3',edgecolor='k',lw=0.6)
    ax.errorbar(x+w/2,fc,yerr=[[fc-flo],[fhi-fc]],color='k',capsize=3,lw=0.8)
    ax.text(x+w/2,fhi*1.08,lab.replace(', ','\n'),ha='center',va='bottom',fontsize=6.8); x+=w
ax.axhline(0.30,color='k',ls=':',lw=1); ax.text(1,0.31,'blended realized price ~$0.30/M (list)',fontsize=7)
ax.axhline(0.06,color='k',ls='--',lw=0.8); ax.text(1,0.063,'effective price, batch+cache heavy users ~$0.03-0.06/M',fontsize=7)
ax.set_xlabel('Share of 2030 inference capacity (%), producers ordered by full cost'); ax.set_ylabel('$ per million tokens'); ax.set_ylim(0,1.0)
ax.set_title('The inference cost curve: marginal cash cost (dark) and full cost incl. carry (light) by producer tier',fontsize=9)
plt.tight_layout(); plt.savefig('f24_coststack.pdf'); print('fig done')
# batch share effect on effective utilization and price
b=T(0.3,0.5,0.7); u_int=T(0.40,0.45,0.50); u_b=T(0.75,0.85,0.92); disc=T(0.25,0.4,0.5)
u_eff=u_int*(1-b)+u_b*b; p_eff=(1-b)+disc*b
print("batch share med",round(m(b),2),"effective utilization",round(m(u_eff),2),"effective price / list",round(m(p_eff),2))
