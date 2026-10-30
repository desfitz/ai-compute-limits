"""Tax check (v28): does tax change the carry comparison? Usage: cd model && python3 tax_check.py
(1) Gross-up: the carry charges an after-tax cost of money (WACC) on net book value; earning that after a tax rate T needs
    r*NB/(1-T) of pre-tax profit, i.e. an extra r*NB*T/(1-T) per year that the base does NOT charge (generous to the build-out).
(2) Deferral: 100% bonus depreciation (OBBBA, P.L. 119-21; IRS Notice 2026-11) writes silicon off for tax at once while books
    depreciate it over its life. The tax not yet paid, T x (book NBV - tax NBV), is an interest-free loan from the Treasury,
    worth r x that balance per year. Shell (buildings) mostly does not qualify; a share of it (power, cooling) may: swept 0-50%.
Plateau path, Big-5 capex as in the base; median of the model's draws."""
import sys, numpy as np
sys.path.insert(0,'.')
import model5 as M
M.N=8000; N=M.N
rng=np.random.default_rng(11); v=M.draw(rng)
capex={**M.HIST,**M.PATHS['Plateau']}
ai={y:np.maximum(capex[y]-v['nonai']*(1+v['gn'])**(y-2023),0)+M.oth_capex(y,capex[y]) for y in M.YEARS}
def nbv(t,c,share,L):
    age=t-c+0.5; G=ai[c]*share
    return np.where(age<L,G*np.maximum(1-age/L,0),0)
for t in (2028,2030,2035):
    si=sum(nbv(t,c,v['phi'],v['Lsi']) for c in M.YEARS if c<=t)
    sh=sum(nbv(t,c,1-v['phi'],v['Lsh']) for c in M.YEARS if c<=t)
    NB=si+sh
    for T in (0.15,0.21):
        gross=v['r']*NB*T/(1-T)
        d0=v['r']*T*si; d50=v['r']*T*(si+0.5*sh)
        print(f"{t} T={T:.2f}: NB {np.median(NB):6.0f} (silicon {np.median(si):5.0f})  gross-up +{np.median(gross):4.0f}  deferral value -{np.median(d0):3.0f} to -{np.median(d50):3.0f}  net +{np.median(gross-d50):4.0f} to +{np.median(gross-d0):4.0f}")
