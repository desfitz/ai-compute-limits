"""Variant runs quoted in the text (v28, all builders): readiness friction off; Goldman opex 2%. Usage: cd model && python3 variants_check.py"""
import sys, numpy as np
sys.path.insert(0,'.')
import model5 as M
M.N=40000
m=np.median
def bu(path,over=None,seed=11):
    rng=np.random.default_rng(seed); v=M.draw(rng,over); H=M.carry(v,path); end,rec,per=M.bottom_up(rng)
    d={t:rec[t]-v['circ']-H[t] for t in M.TY}; return H,d
base={p:bu(p) for p in ('Plateau','Rationalize')}
fr={'fdelay':(0,0,1e-6),'ksite':(1,1,1+1e-6),'pue_up':(0,0,1e-6)}
nofr={p:bu(p,fr) for p in ('Plateau','Rationalize')}
H,d=base['Plateau']; H0,d0=nofr['Plateau']
print("friction effect: carry 2027 %+.0f, 2030 %+.0f; deficit 2030 %+.0f; z %.2f vs %.2f; rationalize P(profit)2030 %.0f%% vs %.0f%%"%(
  m(H[2027])-m(H0[2027]), m(H[2030])-m(H0[2030]), m(d[2030])-m(d0[2030]), m(d[2030])/np.std(d[2030]), m(d0[2030])/np.std(d0[2030]),
  (base['Rationalize'][1][2030]>0).mean()*100,(nofr['Rationalize'][1][2030]>0).mean()*100))
gs={'copex':(0.02,0.02,0.02+1e-6)}
Hg,dg=bu('Plateau',gs)
print("Goldman opex 2%%: 2030 deficit %.0f (base %.0f), z %.2f; carry diff 2028 %.0f, 2030 %.0f"%(m(dg[2030]),m(d[2030]),m(dg[2030])/np.std(dg[2030]),m(H[2028])-m(Hg[2028]),m(H[2030])-m(Hg[2030])))
print("g* friction-off 2030: %.0f%%"%(M.breakeven('Plateau',2030,over=fr)*100))
