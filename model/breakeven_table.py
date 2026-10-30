"""Table of break-even growth g* (Table 'breakeven' in the paper), incl. variants and the cumulative version. Usage: cd model && python3 breakeven_table.py"""
import numpy as np, sys
sys.path.insert(0,'.')
import model5 as M
M.N=20000
def g_star(path,t,over=None,cum=False):
    lo,hi=0.0,2.5
    for _ in range(24):
        mid=(lo+hi)/2; o=M.topdown(path,mid,over=over)
        if cum: val=np.median(sum(o[y]['D']-o[y]['H'] for y in range(2027,t+1)))
        else: val=np.median(o[t]['D']-o[t]['H'])
        lo,hi=(mid,hi) if val<0 else (lo,mid)
    return (lo+hi)/2
fmt=lambda g: '>250%' if g>2.45 else f"{g*100:.0f}%"
rows=[('Plateau','Plateau',None),('Arms race','ArmsRace',None),('Rationalize','Rationalize',None),
      ('Plateau, D2026=163 (low end)','Plateau',{'D0':(163,163,163.001)}),('Plateau, D2026=194 (high end)','Plateau',{'D0':(194,194,194.001)}),
      ('Plateau, accounting lives (4.5-6.5 yr)','Plateau',{'Lsi':(4.5,5.5,6.5)}),('Plateau, 8-year silicon life','Plateau',{'Lsi':(8,8,8.001)}),
      ('Plateau, thermal life Triang(2.5,3.5,5)','Plateau',{'Ltr':(2.5,3.5,5.0)})]
for lab,p,o in rows:
    print(f"{lab:42s} "+"  ".join(fmt(g_star(p,t,o)) for t in (2027,2028,2029,2030)),flush=True)
print("Plateau, cumulative 2027-2030 break-even:",fmt(g_star('Plateau',2030,None,cum=True)))
