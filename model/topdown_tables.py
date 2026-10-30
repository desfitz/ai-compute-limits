"""Tables 'delta' and 'cum' (top-down sweep at fixed g), all builders. Usage: cd model && python3 topdown_tables.py"""
import sys, numpy as np
sys.path.insert(0,'.')
import model5 as M
M.N=40000
m=np.median; q=np.percentile
for g in (0.2,0.3,0.4,0.5,0.6,0.8):
    o=M.topdown('Plateau',g)
    print(f"g={g:.0%} "+" ".join(f"{t}:{m(o[t]['D']-o[t]['H']):.0f}({((o[t]['D']-o[t]['H'])<0).mean()*100:.0f}%)" for t in (2027,2028,2029,2030)),flush=True)
for p in ('Plateau','ArmsRace','Rationalize'):
    row=[]
    for g in (0.3,0.5,0.7):
        o=M.topdown(p,g); c=sum(o[t]['D']-o[t]['H'] for t in (2027,2028,2029,2030))
        row.append(f"{m(c):.0f} ({q(c,10):.0f},{q(c,90):.0f}; {(c<0).mean()*100:.0f}%)")
    print(p,' | '.join(row),flush=True)
