"""Regenerate every headline number and figure from parameters.json. Usage: python3 rebuild.py -> numbers.json + figures + delta vs last run."""
import json, os, subprocess, numpy as np, sys
from model5 import *
m=np.median; q=lambda x,p: np.percentile(x,p)
out={"as_of":json.load(open('parameters.json'))['_meta']['as_of']}
for p in PATHS:
    r=run(p); d={t:r['rec'][t]-r['circ']-r['H'][t] for t in TY}
    out[p]={"H":{t:round(float(m(r['H'][t]))) for t in TY},"receipts":{t:round(float(m(r['rec'][t]))) for t in TY},
            "delta":{t:round(float(m(d[t]))) for t in TY},"P_profit":{t:round(float((d[t]>0).mean()*100)) for t in TY},
            "g_star":{t:round(breakeven(p,t)*100) for t in (2028,2029,2030)}}
rng=np.random.default_rng(11); v=draw(rng); H=carry(v,'Plateau'); end,rec,per=bottom_up(rng); d=rec[2030]-v['circ']-H[2030]
out["plateau_2030"]={"delta":round(float(m(d))),"sigma":round(float(np.std(d))),"z":round(float(m(d)/np.std(d)),2),"end_customer":round(float(m(end[2030]))),"receipts":round(float(m(rec[2030])))}
ra=adaptive(); out["Adaptive"]={"capex":{t:round(float(m(ra['capex'][t]))) for t in TY},"delta":{t:round(float(m(ra['d'][t]))) for t in TY}}
prev=json.load(open('numbers.json')) if os.path.exists('numbers.json') else None
json.dump(out,open('numbers.json','w'),indent=1,default=str)
# reissue test
if prev:
    dz=out['plateau_2030']['z']-prev['plateau_2030']['z']; dg=out['Plateau']['g_star'][2030]-prev['Plateau']['g_star']['2030']
    dp=out['Rationalize']['P_profit'][2030]-prev['Rationalize']['P_profit']['2030']
    material=abs(dz)>=0.5 or abs(dg)>=5 or abs(dp)>=15
    print(f"DELTA vs previous: z {dz:+.2f}, g*2030 {dg:+d} pts, P(profit|rationalize,2030) {dp:+d} pts -> {'MATERIAL: re-release with delta log' if material else 'minor: update tables, bump version'}")
else: print("first run; numbers.json written")
print("Plateau 2030:",out['plateau_2030'],"| g*:",out['Plateau']['g_star'])
if '--figs' in sys.argv:
    for f in ['figs4.py','figs5.py','decomp.py','overlap.py','figs16.py','incumbent.py']: subprocess.run(['python3',f],stdout=subprocess.DEVNULL)
    print("figures regenerated")
