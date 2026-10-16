"""Dependency graph of the estimate: register inputs -> derived quantities -> outputs. Regenerate: python3 blueprint.py"""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams.update({'font.size':7.5})
# nodes: (name, column, row, kind)  kind: in=input (register), d=derived, o=output, s=secondary
cols={0:0.02,1:0.30,2:0.58,3:0.84}
nodes={
 # supply inputs
 'capex_history':(0,0.96,'in'),'ai_capex_2023':(0,0.91,'in'),'nonai_growth':(0,0.86,'in'),'silicon_share':(0,0.81,'in'),
 'training_share':(0,0.76,'in'),'life_training':(0,0.71,'in'),'life_inference':(0,0.66,'in'),'life_shell':(0,0.61,'in'),
 'lag_silicon/shell':(0,0.56,'in'),'opex_share':(0,0.51,'in'),'cooling_uplift':(0,0.46,'in'),'wacc':(0,0.41,'in'),
 'grid_cap':(0,0.36,'in'),'siting_deferral':(0,0.31,'in'),'site_cost_uplift':(0,0.26,'in'),
 # demand inputs
 'base_2026 (7 comps)':(0,0.19,'in'),'theta (by channel)':(0,0.14,'in'),'sector R,C,k,theta_s':(0,0.09,'in'),'eu_displacement':(0,0.04,'in'),
 'common factors':(0,-0.01,'in'),'circular':(0,-0.06,'in'),'residual factor':(0,-0.11,'s'),
 # feasibility inputs
 'software/services pools':(0,-0.18,'in'),'seat_saas_growth':(0,-0.23,'s'),'reallocation_to_ai':(0,-0.28,'s'),'eu_pool_displacement':(0,-0.33,'in'),
 # derived
 'N_c baseline':(1,0.88,'d'),'A_c AI capex':(1,0.80,'d'),'L_si effective':(1,0.70,'d'),'energized cohorts':(1,0.55,'d'),'deferred capital':(1,0.45,'d'),
 'carry H_t':(1,0.33,'d'),
 'top-down D_t':(1,0.17,'d'),'bottom-up R_s(t)':(1,0.09,'d'),'infra receipts':(1,0.00,'d'),
 'feasibility band':(1,-0.25,'d'),
 # outputs
 'delta_t, P(profit)':(2,0.28,'o'),'z-score':(2,0.20,'o'),'break-even g*':(2,0.12,'o'),'probability map':(2,0.02,'o'),
 'variance budget':(2,-0.08,'o'),'horizon 2035 / adaptive':(2,-0.18,'o'),'incumbent case':(2,-0.30,'o'),
 'paper tables & figures':(3,0.10,'o'),'re-issue rule':(3,-0.05,'o'),
}
edges=[('capex_history','A_c AI capex'),('ai_capex_2023','N_c baseline'),('nonai_growth','N_c baseline'),('N_c baseline','A_c AI capex'),
 ('silicon_share','energized cohorts'),('training_share','L_si effective'),('life_training','L_si effective'),('life_inference','L_si effective'),
 ('life_shell','carry H_t'),('L_si effective','carry H_t'),('lag_silicon/shell','energized cohorts'),('A_c AI capex','energized cohorts'),
 ('grid_cap','deferred capital'),('siting_deferral','deferred capital'),('energized cohorts','carry H_t'),('deferred capital','carry H_t'),
 ('opex_share','carry H_t'),('cooling_uplift','carry H_t'),('wacc','carry H_t'),('site_cost_uplift','carry H_t'),
 ('base_2026 (7 comps)','top-down D_t'),('theta (by channel)','top-down D_t'),('base_2026 (7 comps)','bottom-up R_s(t)'),('sector R,C,k,theta_s','bottom-up R_s(t)'),
 ('eu_displacement','bottom-up R_s(t)'),('common factors','bottom-up R_s(t)'),('bottom-up R_s(t)','infra receipts'),('circular','infra receipts'),('residual factor','infra receipts'),
 ('carry H_t','delta_t, P(profit)'),('infra receipts','delta_t, P(profit)'),('top-down D_t','break-even g*'),('carry H_t','break-even g*'),
 ('delta_t, P(profit)','z-score'),('delta_t, P(profit)','probability map'),('feasibility band','probability map'),('residual factor','probability map'),
 ('software/services pools','feasibility band'),('seat_saas_growth','feasibility band'),('reallocation_to_ai','feasibility band'),('eu_pool_displacement','feasibility band'),
 ('carry H_t','variance budget'),('infra receipts','variance budget'),('carry H_t','horizon 2035 / adaptive'),('bottom-up R_s(t)','horizon 2035 / adaptive'),
 ('seat_saas_growth','incumbent case'),('z-score','paper tables & figures'),('break-even g*','paper tables & figures'),('probability map','paper tables & figures'),
 ('variance budget','paper tables & figures'),('horizon 2035 / adaptive','paper tables & figures'),('incumbent case','paper tables & figures'),
 ('z-score','re-issue rule'),('break-even g*','re-issue rule'),('delta_t, P(profit)','re-issue rule')]
fig,ax=plt.subplots(figsize=(13,10.5)); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(-0.38,1.0)
fc={'in':'0.93','d':'0.80','o':'0.62','s':'1.0'}; ec={'in':'0.4','d':'0.2','o':'0','s':'0'}
pos={}
for n,(c,y,k) in nodes.items():
    x=cols[c]; w=0.16 if c<3 else 0.14; pos[n]=(x,y,w)
    ax.add_patch(FancyBboxPatch((x,y-0.017),w,0.034,boxstyle='round,pad=0.004',fc=fc[k],ec=ec[k],lw=1.2 if k=='s' else 0.8,ls='--' if k=='s' else '-'))
    ax.text(x+w/2,y,n,ha='center',va='center',fontsize=7)
for a,b in edges:
    xa,ya,wa=pos[a]; xb,yb,wb=pos[b]
    ax.add_patch(FancyArrowPatch((xa+wa,ya),(xb,yb),arrowstyle='-|>',mutation_scale=7,lw=0.5,color='0.35',connectionstyle='arc3,rad=0.05'))
for c,t in zip(range(4),['REGISTER INPUTS (parameters.json)','DERIVED QUANTITIES (model5.py)','OUTPUTS (numbers.json)','RENDERINGS']):
    ax.text(cols[c]+0.08 if c<3 else cols[c]+0.07,0.995,t,ha='center',fontsize=8,fontweight='bold')
ax.text(0.02,-0.365,'Dashed boxes: secondary variables (swept in their own figures, not trusted at a range). A change to any input propagates along the arrows; CI recomputes the outputs and applies the re-issue rule.',fontsize=7.5)
plt.tight_layout(); plt.savefig('blueprint.pdf'); plt.savefig('blueprint.png',dpi=130); print('blueprint written')
