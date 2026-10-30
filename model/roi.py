"""Return on the money invested, year by year, and the cumulative deficit with and without the cost of money on the losses (v28). Usage: cd model && python3 roi.py"""
import sys, numpy as np
sys.path.insert(0,'.')
import model5 as M
M.N=40000
from model5 import *
N=M.N
def carry2(v,capex_path):
    capex={**M.HIST,**capex_path}
    ai={y:np.maximum(capex[y]-v['nonai']*(1+v['gn'])**(y-2023),0) for y in M.YEARS}
    defer=np.zeros(N); aiE={}; aiD={}
    for y in M.YEARS:
        tot=ai[y]+defer; e=np.minimum(tot,v['gridcap'])*(1-v['fdelay']) if y>=2026 else np.minimum(tot,v['gridcap'])
        aiE[y]=e; aiD[y]=tot-e; defer=tot-e
    H={};NB={}
    for t in M.TY:
        dep=np.zeros(N); gross=np.zeros(N); net=np.zeros(N)
        for c in M.YEARS:
            if c>t: continue
            age=t-c+0.5
            for share,L,lg,ku in ((v['phi'],v['Lsi'],v['lagsi'],1.0),(1-v['phi'],v['Lsh'],v['lagsh'],v['ksite'])):
                f=lg if c==t else 1.0
                G=aiE[c]*f*share*ku; alive=age<L
                dep+=np.where(alive,G/L,0); gross+=np.where(alive,G,0); net+=np.where(alive,G*np.maximum(1-age/L,0),0)
        nb=net+aiD.get(t,0)
        H[t]=dep+v['copex']*(1+v['pue_up'])*gross+v['r']*nb; NB[t]=nb
    return H,NB
m=np.median
for path in ['Plateau','ArmsRace','Rationalize','Adaptive']:
    rng=np.random.default_rng(11); v=M.draw(rng); end,rec,per=M.bottom_up(rng)
    if path!='Adaptive':
        H,NB=carry2(v,M.PATHS[path])
    else:
        a=0.5;lo,hi=400,1100;capex={};H={};NB={}
        for t in range(2027,2036):
            capex[t]=np.full(N,780.) if t==2027 else np.clip(capex[t-1]*((rec[t-1]-v['circ'])/H[t-1])**a,lo,hi)
            p={y:(capex[y] if y in capex else 780.) for y in range(2027,2036)}
            Ht,NBt=carry2(v,p); H[t]=Ht[t]; NB[t]=NBt[t]
    cum=np.zeros(N); comp=np.zeros(N); sumret=np.zeros(N); sumnb=np.zeros(N)
    print(path)
    for t in range(2027,2036):
        d=rec[t]-v['circ']-H[t]
        cum+=d; comp=comp*(1+v['r'])+d
        realized=v['r']+d/NB[t]
        sumret+=v['r']*NB[t]+d; sumnb+=NB[t]
        print(f"  {t}: NB {m(NB[t]):6.0f}  delta {m(d):6.0f}  cum {m(cum):7.0f}  cum@wacc {m(comp):7.0f}  realized {m(realized)*100:5.1f}%  avg-to-date {m(sumret/sumnb)*100:5.1f}%")
print("wacc median",m(v['r']))
