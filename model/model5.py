import numpy as np, json, os
_P=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'parameters.json'))) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),'parameters.json')) else {}
def _reg(section,key,default):
    try: v=_P[section][key]['value']; return tuple(v) if isinstance(v,list) else v
    except Exception: return default
N=100_000
HIST={int(k):v for k,v in _reg('supply','capex_history',{'2023':161,'2024':260,'2025':448,'2026':780}).items()}
PATHS={'Plateau':{y:780 for y in range(2027,2036)},
       'ArmsRace':{2027:1000,**{y:1100 for y in range(2028,2036)}},
       'Rationalize':{2027:550,**{y:500 for y in range(2028,2036)}}}
YEARS=list(range(2023,2036)); TY=range(2027,2036)
HORIZON=2030
def adaptive(seed=11,a=0.5,lo=400,hi=1100,cap0=780,kappa=1.0,gamma=0.0):
    """Rational-operator path: next year's capex scales with last year's receipts/carry ratio, damped (a) and bounded."""
    rng=np.random.default_rng(seed); v=draw(rng); end,rec,per=bottom_up(rng,kappa,gamma)
    capex={}; H={}
    for t in range(2027,2036):
        capex[t]=np.full(N,float(cap0)) if t==2027 else np.clip(capex[t-1]*((rec[t-1]-v['circ'])/H[t-1])**a,lo,hi)
        PATHS['_adapt']={y:(capex[y] if y in capex else cap0) for y in range(2027,2036)}
        H[t]=kappa*carry(v,'_adapt')[t]
    PATHS.pop('_adapt',None)
    d={t:rec[t]-v['circ']-H[t] for t in range(2027,2036)}
    return dict(capex=capex,H=H,rec=rec,end=end,d=d,circ=v['circ'])   # tables in the body use 2027-2030; Appendix E uses 2031-2035
def T(rng,a,b,c): return rng.triangular(a,b,c,N)
# ---- Bottom-up sectors: (R26 base $B, 2030 ceiling $B, logistic k, cloud-capture share theta, sovereign-exposed?)
SECTORS={
 'Coding tools':          dict(R=(15,20,28),  C=(40,60,90),    k=(0.6,0.9,1.3), th=(0.7,0.8,0.9), sov=0),
 'Office assistants/agents':dict(R=(20,30,45),  C=(100,150,230), k=(0.5,0.8,1.1), th=(0.45,0.6,0.75),sov=1),
 'Customer service/CX':   dict(R=(5,8,12),    C=(25,40,60),    k=(0.5,0.8,1.2), th=(0.35,0.5,0.65),sov=1),
 'Consumer subscriptions':dict(R=(18,25,35),  C=(50,64,80),   k=(0.5,0.8,1.2), th=(0.75,0.85,0.95),sov=0),
 'Advertising uplift':    dict(R=(25,40,55),  C=(105,136,170),  k=(0.4,0.7,1.0), th=(0.9,1.0,1.0), sov=0),
 'Search & internal use': dict(R=(12,20,30),  C=(30,50,80),    k=(0.4,0.7,1.0), th=(0.9,1.0,1.0), sov=0),
 'Financial services':    dict(R=(6,10,15),   C=(25,40,60),    k=(0.4,0.7,1.0), th=(0.6,0.75,0.9), sov=1),
 'Healthcare/clinical':   dict(R=(4,6,9),     C=(20,35,50),    k=(0.3,0.5,0.8), th=(0.5,0.65,0.8), sov=1),
 'Legal & compliance':    dict(R=(3,5,8),     C=(12,20,30),    k=(0.3,0.5,0.8), th=(0.5,0.65,0.8), sov=1),
 'Public sector/defense': dict(R=(5,8,12),    C=(25,40,60),    k=(0.3,0.5,0.8), th=(0.7,0.85,1.0), sov=1),
 'Autonomous fleets':     dict(R=(5,8,12),    C=(16,27,43),    k=(0.3,0.5,0.8), th=(0.3,0.45,0.6), sov=0),
 'Gen video/gaming/media':dict(R=(5,8,12),    C=(17,26,37),    k=(0.4,0.7,1.0), th=(0.8,0.9,1.0), sov=0),
 'Factory/robotics sw':   dict(R=(2,4,6),     C=(8,15,25),     k=(0.3,0.5,0.8), th=(0.3,0.45,0.6), sov=0),
 'Science/R&D':           dict(R=(2,4,7),     C=(10,25,45),    k=(0.4,0.7,1.0), th=(0.7,0.85,1.0), sov=1),
 'Eldercare/assistive':   dict(R=(0.5,1,2),   C=(3,6,12),      k=(0.3,0.5,0.8), th=(0.1,0.15,0.25),sov=0),
}
def draw(rng,over=None):
    R=lambda sec,k,d: _reg(sec,k,d)
    p=dict(ai23=R('supply','ai_capex_2023',(20,30,40)),gn=R('supply','nonai_growth',(0.02,0.06,0.10)),phi=R('supply','silicon_share',(0.45,0.52,0.60)),
           gridcap=R('supply','grid_cap',(1150,1400,1680)),fdelay=R('supply','siting_deferral',(0.10,0.20,0.35)),ksite=R('supply','site_cost_uplift',(1.02,1.05,1.09)),pue_up=R('supply','cooling_opex_uplift',(0.00,0.03,0.06)),
           ftrain=R('supply','training_share',(0.35,0.45,0.55)),Ltr=R('supply','life_training',(2.5,3.5,4.5)),Linf=R('supply','life_inference',(4.0,5.0,6.0)),Lsh=R('supply','life_shell',(15,20,25)),
           copex=R('supply','opex_share',(0.059,0.0665,0.074)),r=R('supply','wacc',(0.090,0.0945,0.099)),lagsi=R('supply','lag_silicon',(0.5,0.7,0.9)),lagsh=R('supply','lag_shell',(0.2,0.4,0.6)),
           D0=R('demand','base_2026',(163,179,194)),theta=R('demand','theta',(0.77,0.815,0.86)),circ=R('demand','circular',(8,12,18)))
    if over:
        if 'Lsi' in over: over=dict(over); L=over.pop('Lsi'); p['Ltr']=L; p['Linf']=L
        p.update(over)
    v={k:T(rng,*p[k]) for k in p}
    v['Lsi']=1.0/(v['ftrain']/v['Ltr']+(1-v['ftrain'])/v['Linf'])
    v['lag']=v['phi']*v['lagsi']+(1-v['phi'])*v['lagsh']
    v['nonai']=161-v['ai23']          # 2023 baseline, constrained by flat 2023 total capex
    return v
def carry(v,path):
    capex={**HIST,**PATHS[path]}
    ai={y:np.maximum(capex[y]-v['nonai']*(1+v['gn'])**(y-2023),0) for y in YEARS}
    # grid interconnection cap: AI capex above the energizable ceiling is deferred to the next year (carries return only)
    defer=np.zeros(N); aiE={}; aiD={}
    for y in YEARS:
        tot=ai[y]+defer; e=np.minimum(tot,v['gridcap'])*(1-v['fdelay']) if y>=2026 else np.minimum(tot,v['gridcap'])
        aiE[y]=e; aiD[y]=tot-e; defer=tot-e
    ai=aiE; H={}
    for t in TY:
        dep=np.zeros(N); gross=np.zeros(N); net=np.zeros(N)
        for c in YEARS:
            if c>t: continue
            age=t-c+0.5
            for share,L,lg,ku in ((v['phi'],v['Lsi'],v['lagsi'],1.0),(1-v['phi'],v['Lsh'],v['lagsh'],v['ksite'])):
                f=lg if c==t else 1.0
                G=ai[c]*f*share*ku; alive=age<L
                dep+=np.where(alive,G/L,0); gross+=np.where(alive,G,0); net+=np.where(alive,G*np.maximum(1-age/L,0),0)
        H[t]=dep+v['copex']*(1+v['pue_up'])*gross+v['r']*net+v['r']*aiD.get(t,0)
    return H
def bottom_up(rng,kappa=1.0,gamma=0.0):
    """returns end-customer demand by sector/year and cloud receipts by year"""
    end={t:np.zeros(N) for t in range(2026,2036)}; rec={t:np.zeros(N) for t in range(2026,2036)}; per={}
    mC=T(rng,*_reg('demand','common_factor_ceiling',(0.7,1.0,1.4))); mk=T(rng,*_reg('demand','common_factor_ramp',(0.7,1.0,1.3)))   # common macro-adoption factors
    gC=T(rng,*_reg('demand','post2030_ceiling_growth',(0.06,0.10,0.14)))
    geu=T(rng,*_reg('demand','eu_displacement',(0.03,0.05,0.08)))                       # European sovereignty displacement of US vendors by 2030, share of global sovereign-exposed demand
    _bs=_reg('demand','base_2026',(163,179,194)); _scale=_bs[1]/179.0   # sector 2026 bases track the registered base
    for s,q in SECTORS.items():
        R=T(rng,*q['R'])*_scale; C=np.maximum(T(rng,*q['C'])*mC,R*1.05); k=T(rng,*q['k'])*mk; th=T(rng,*q['th'])
        per[s]={}
        for t in range(2026,2036):
            Ct=C*np.where(t>2030,(1+gC)**(t-2030),1.0)
            x=Ct/(1+(Ct/R-1)*np.exp(-k*(t-2026)))
            g=(1-gamma)*(1-geu*min(max(t-2026,0),4)/4) if q['sov'] else 1.0
            per[s][t]=x*g; end[t]+=x*g; rec[t]+=x*g*th
    return end,rec,per
def run(path,kappa=1.0,gamma=0.0,seed=11):
    rng=np.random.default_rng(seed); v=draw(rng); H=carry(v,path); end,rec,per=bottom_up(rng,kappa,gamma)
    return dict(H={t:kappa*H[t]-0 for t in TY},end=end,rec=rec,per=per,circ=v['circ'])
def topdown(path,g,seed=7,over=None):
    rng=np.random.default_rng(seed); v=draw(rng,over); H=carry(v,path)
    return {t:dict(H=H[t],D=v['theta']*v['D0']*(1+g)**(t-2026)) for t in TY}
def breakeven(path,t,over=None):
    lo,hi=0.0,1.5
    for _ in range(28):
        m=(lo+hi)/2; o=topdown(path,m,over=over)[t]; lo,hi=(m,hi) if np.median(o['D']-o['H'])<0 else (lo,m)
    return (lo+hi)/2
if __name__=='__main__':
    q=lambda x,p: np.percentile(x,p); m=np.median
    r=run('Plateau')
    print("Bottom-up END demand by year:",{t:f"{m(r['end'][t]):.0f} ({q(r['end'][t],10):.0f}-{q(r['end'][t],90):.0f})" for t in r['end']})
    print("Bottom-up CLOUD receipts:",{t:f"{m(r['rec'][t]):.0f} ({q(r['rec'][t],10):.0f}-{q(r['rec'][t],90):.0f})" for t in r['rec']})
    e=r['end']; print("implied g by year:",{t:f"{m(e[t]/e[t-1])-1:.0%}" for t in range(2027,2031)}, "CAGR 26-30:",f"{m((e[2030]/e[2026])**0.25)-1:.0%}")
    print("Sector medians 2026 / 2030:")
    for s in SECTORS: print(f"  {s:24s} {m(r['per'][s][2026]):6.1f} -> {m(r['per'][s][2030]):6.1f}")
    for path in PATHS:
        for kap,gam,lab in [(1.0,0.0,'no sov'),(1.2,0.25,'sov')]:
            r=run(path,kap,gam); 
            d={t:r['rec'][t]-r['circ']-r['H'][t] for t in TY}
            print(f"{path:12s} {lab:7s}: "+"  ".join(f"{t}: {m(d[t]):+.0f} ({(d[t]<0).mean()*100:.0f}%)" for t in TY),
                  f" cum {m(sum(d.values())):+.0f} P<0 {(sum(d.values())<0).mean()*100:.0f}%")
    print("Top-down g*:",{p:{t:f"{breakeven(p,t)*100:.0f}%" for t in TY} for p in PATHS})
