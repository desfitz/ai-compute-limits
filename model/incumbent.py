import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
N=100_000; rng=np.random.default_rng(88); T=lambda a,b,c: rng.triangular(a,b,c,N)
q=lambda x,p: np.percentile(x,p); m=np.median
# ---- Microsoft 365 commercial: worked incumbent case, 2026 -> 2030
seats26=T(420,450,480)            # M commercial paid seats (verify)
arpu26=T(19,21,23)                # $/seat/month blended commercial (verify)
rev26=seats26*arpu26*12/1000      # $B
price_g=T(0.05,0.08,0.12)         # list-price growth/yr incl. July-2026 hike and bundling
elast=T(0.15,0.35,0.60)           # seats lost per unit of price increase (dimensionless elasticity)
agent_seat=T(-0.06,-0.03,0.00)    # seat change/yr from agents replacing human seats
eu_exit=T(0.03,0.08,0.15)         # cumulative EU/sovereignty seat loss by 2030
seats30=seats26*(1+agent_seat)**4*(1-eu_exit)*(1-elast*((1+price_g)**4-1))
arpu30=arpu26*(1+price_g)**4
base30=seats30*arpu30*12/1000
attach=T(0.12,0.22,0.35)          # Copilot paid attach on remaining seats by 2030 (20M/450M=4.4% today)
cop_price=T(24,30,36)
cop30=seats30*attach*cop_price*12/1000
agent_cons=T(0.3,0.6,1.0)         # agentic consumption relative to Copilot seat revenue
tot30=base30+cop30*(1+agent_cons)
print("M365 2026 rev med",round(m(rev26)),"| 2030 base (ex-Copilot) med",round(m(base30)),"P10-P90",round(q(base30,10)),round(q(base30,90)))
print("  seats30 med",round(m(seats30)),"arpu30",round(m(arpu30),1),"| Copilot+agents med",round(m(cop30*(1+agent_cons))),"| total 2030 med",round(m(tot30)),"P10-P90",round(q(tot30,10)),round(q(tot30,90)))
print("  P(base30 < rev26)",round((base30<rev26).mean()*100),"%   P(total30 < rev26)",round((tot30<rev26).mean()*100),"%   P(total30 < rev26*1.08^4)",round((tot30<rev26*1.08**4).mean()*100),"% (below an 8%/yr trend)")
# ---- generic seat vendor: does price-up offset seat-down?  revenue ratio 2030/2026 vs seat decline and price growth
fig,ax=plt.subplots(1,2,figsize=(11,3.6))
sd=np.linspace(-0.10,0.02,13); pg=[0.04,0.08,0.12]
for p,ls in zip(pg,[':','-','--']):
    ratio=[((1+s_)**4*(1-0.35*((1+p)**4-1))*(1+p)**4) for s_ in sd]
    ax[0].plot(sd*100,ratio,ls,color='k',label=f'price +{p:.0%}/yr, elasticity 0.35')
ax[0].axhline(1,color='gray',lw=0.8); ax[0].set_xlabel('Seat change from agents and sovereignty (%/yr)'); ax[0].set_ylabel('Seat revenue 2030 / 2026'); ax[0].legend(fontsize=7)
ax[0].set_title('The incumbent arithmetic: can price offset seats?',fontsize=9)
ax[1].hist(tot30,bins=80,color='0.6',alpha=0.9,label='2030 total incl. Copilot & agents'); ax[1].hist(base30,bins=80,color='0.25',alpha=0.7,label='2030 base (ex-Copilot)')
ax[1].axvline(m(rev26),color='k',ls='--',label=f'2026 revenue (~${m(rev26):.0f}B)'); ax[1].axvline(m(rev26)*1.08**4,color='k',ls=':',label='8%/yr trend')
ax[1].set_xlabel('Microsoft 365 commercial revenue 2030 ($B)'); ax[1].set_yticks([]); ax[1].legend(fontsize=7); ax[1].set_title('Worked case: Microsoft 365 commercial, 2030',fontsize=9)
plt.tight_layout(); plt.savefig('f21_incumbent.pdf')
# ---- secondary variables: reallocation share and seat-SaaS growth -> feasibility band
sw26=T(1.38,1.44,1.50)*1000; sv26=T(1.80,1.87,1.94)*1000; seat_share=T(0.50,0.55,0.60)
infra30=sw26*(1-seat_share)*(1+T(0.04,0.08,0.12))**4; sv30=sv26*(1+T(-0.02,0.03,0.07))**4
eu=T(0.20,0.23,0.26)*T(0.10,0.20,0.35)+T(0.08,0.10,0.12)*T(0.7,0.85,0.95)
ads=T(140,170,200); cons=T(80,105,130); ainew=T(0.02,0.04,0.07)
fig,ax=plt.subplots(1,2,figsize=(11,3.4))
rs=np.linspace(0.08,0.40,9)
for gs,ls,lab in [(-0.06,':','seat SaaS -6%/yr'),(0.0,'-','seat SaaS 0%/yr'),(0.05,'--','seat SaaS +5%/yr')]:
    seat30=sw26*seat_share*(1+gs)**4; pool=(seat30+infra30+sv30)*(1-eu)
    med=[m(pool*(r+ainew)+ads+cons) for r in rs]; lo=[q(pool*(r+ainew)+ads+cons,10) for r in rs]; hi=[q(pool*(r+ainew)+ads+cons,90) for r in rs]
    ax[0].plot(rs*100,med,ls,color='k',label=lab)
    if gs==0.0: ax[0].fill_between(rs*100,lo,hi,color='gray',alpha=0.25)
ax[0].axhline(950,color='k',lw=1,ls='-.'); ax[0].text(9,965,'plateau 50%-probability contour (~$950B)',fontsize=7)
ax[0].set_xlabel('Share of accessible pool reallocated to AI solutions by 2030 (%)'); ax[0].set_ylabel('Feasibility cutoff, total 2030 AI revenue ($B)'); ax[0].legend(fontsize=7)
ax[0].set_title('Secondary variable 1: reallocation share (band = P10-P90 at 0%/yr)',fontsize=9)
gss=np.linspace(-0.10,0.06,9); disp=np.linspace(0.0,0.5,6)
for d_,ls in zip([0.0,0.2,0.4],[':','-','--']):
    eu2=T(0.20,0.23,0.26)*d_+T(0.08,0.10,0.12)*T(0.7,0.85,0.95)
    vals=[]
    for gs in gss:
        seat30=sw26*seat_share*(1+gs)**4; pool=(seat30+infra30+sv30)*(1-eu2); vals.append(m(pool*(T(0.12,0.20,0.32)+ainew)+ads+cons))
    ax[1].plot(gss*100,vals,ls,color='k',label=f'EU displacement {d_:.0%}')
ax[1].axhline(950,color='k',lw=1,ls='-.'); ax[1].set_xlabel('Seat-priced SaaS growth 2026-30 (%/yr)'); ax[1].set_ylabel('Feasibility cutoff ($B)'); ax[1].legend(fontsize=7)
ax[1].set_title('Secondary variable 2: seat deflation x sovereignty displacement',fontsize=9)
plt.tight_layout(); plt.savefig('f22_secondary.pdf'); print('figs done')
