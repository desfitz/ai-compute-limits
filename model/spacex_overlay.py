"""SpaceX/xAI as a sixth builder (v28 overlay, outside the base case). Usage: cd model && python3 spacex_overlay.py
Runs SpaceX's AI capex through the same vintage carry as the Big-5 (same lives, lags, opex, WACC draws).
AI capex: 2023 0.5, 2024 5.6, 2025 12.7 (IPO filing / Q2 call); 2026 = 7.7 + 15.8 + 16.4 + Q4 (guided total 35-40, 'almost entirely' compute; 32-37 taken as AI) ~ 74.5.
Two forward paths: 'hold' at the 2026 level; 'Q4 pace' at ~150/yr from 2027.
No receipts are added: SpaceX's rent from Anthropic and its Grok/Cursor revenue already sit inside the receipts the model counts."""
import sys, numpy as np
sys.path.insert(0,'.')
import model5 as M
M.N=8000
N=M.N
HIST={2023:0.5,2024:5.6,2025:12.7,2026:74.5}
def carry(v,path):
    capex={**HIST,**path}; H={}
    for t in M.TY:
        dep=np.zeros(N); gross=np.zeros(N); net=np.zeros(N)
        for c in M.YEARS:
            if c>t: continue
            age=t-c+0.5
            for share,L,lg,ku in ((v['phi'],v['Lsi'],v['lagsi'],1.0),(1-v['phi'],v['Lsh'],v['lagsh'],v['ksite'])):
                f=lg if c==t else 1.0
                G=capex[c]*f*share*ku; alive=age<L
                dep+=np.where(alive,G/L,0); gross+=np.where(alive,G,0); net+=np.where(alive,G*np.maximum(1-age/L,0),0)
        H[t]=dep+v['copex']*(1+v['pue_up'])*gross+v['r']*net
    return H
rng=np.random.default_rng(11); v=M.draw(rng)
for name,lvl in (('hold at 2026 level (~$75B/yr)',74.5),('Q4 pace (~$150B/yr)',150.0)):
    H=carry(v,{y:lvl for y in range(2027,2036)})
    print(name, ' '.join(f"{t}:{np.median(H[t]):.0f}" for t in (2027,2028,2030,2035)))
