"""Table 'bu_results': bottom-up median Delta_t and P(Delta<0), with and without the sovereignty overlay (all builders). Usage: cd model && python3 bu_table.py"""
import sys, numpy as np
sys.path.insert(0,'.')
import model5 as M
M.N=40000
m=np.median
for path in ('Plateau','ArmsRace','Rationalize'):
    for kap,gam,lab in ((1.0,0.0,'none'),(1.2,0.25,'sov')):
        r=M.run(path,kap,gam); d={t:r['rec'][t]-r['circ']-r['H'][t] for t in range(2027,2031)}; c=sum(d.values())
        print(path,lab,' '.join(f"{t}:{m(d[t]):.0f}({(d[t]<0).mean()*100:.0f}%)" for t in d),f"cum:{m(c):.0f}({(c<0).mean()*100:.0f}%)",flush=True)
