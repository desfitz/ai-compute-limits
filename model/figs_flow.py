"""Figure: where an AI customer dollar goes (colour, every box and arrow labelled). v28. Usage: python3 figs_flow.py -> f18_flow.pdf"""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
C=dict(cust='#DCEBFA',lab='#E7DDF7',hyp='#D9F0E3',ads='#FCE9D2',infra='#C9DDF5',leak='#F6D7D7',inv='#FFF3C4',edge='#33415C')
fig,ax=plt.subplots(figsize=(9,5.2)); ax.axis('off'); ax.set_xlim(-0.005,1.005); ax.set_ylim(-0.17,1)
def box(x,y,w,h,title,body,fc):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012,rounding_size=0.02',fc=fc,ec=C['edge'],lw=1.2))
    ax.text(x+w/2,y+h-0.035,title,ha='center',va='top',fontsize=9.5,fontweight='bold',color='#1E2761')
    ax.text(x+w/2,y+h-0.09,body,ha='center',va='top',fontsize=8.3,color='#1F1F1F',linespacing=1.35)
def arrow(x1,y1,x2,y2,label,lx=None,ly=None,col='#1E2761',ls='-',rad=0.0):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=16,lw=1.8,color=col,linestyle=ls,connectionstyle=f'arc3,rad={rad}'))
    lx=(x1+x2)/2 if lx is None else lx; ly=(y1+y2)/2 if ly is None else ly
    ax.text(lx,ly,label,ha='center',va='center',fontsize=7.8,color=col,bbox=dict(boxstyle='round,pad=0.2',fc='white',ec='none',alpha=0.95))
box(0.01,0.33,0.19,0.34,'END CUSTOMERS','enterprises, consumers,\nadvertisers pay\nrevenue $D_t$\n(about \\$179B\nin 2026)',C['cust'])
box(0.36,0.71,0.21,0.22,'FRONTIER LABS','OpenAI, Anthropic, others:\nkeep a margin, buy\ncompute with the rest',C['lab'])
box(0.36,0.39,0.21,0.22,'HYPERSCALER AI SERVICES','Azure AI, Bedrock,\nVertex, Copilot seats',C['hyp'])
box(0.36,0.07,0.21,0.22,'ADVERTISING & CONSUMER','Meta and Google ads,\nsubscriptions',C['ads'])
box(0.76,0.39,0.23,0.24,'INFRASTRUCTURE OWNERS','the Big-5 data centers;\nreceipts about\n\\$480-490B by 2030',C['infra'])
box(0.76,0.74,0.23,0.19,'INVESTOR CAPITAL','lab equity, \\$190B\nin 2026; not revenue',C['inv'])
box(0.76,0.04,0.23,0.17,'LEAKAGE','on-device chips, on-premise,\nintegrators, open models',C['leak'])
arrow(0.20,0.60,0.36,0.80,'lab channel ~50%',0.27,0.74)
arrow(0.20,0.50,0.36,0.50,'direct ~20%',0.28,0.53)
arrow(0.20,0.40,0.36,0.19,'ads & consumer ~30%',0.27,0.27)
arrow(0.57,0.80,0.76,0.56,'compute spend:\n0.64 of each dollar',0.665,0.71)
arrow(0.57,0.50,0.76,0.50,'all of it',0.665,0.475)
arrow(0.57,0.19,0.76,0.44,'85-100%',0.665,0.30)
arrow(0.83,0.74,0.83,0.63,'pays for lab\ncompute early',0.92,0.685,col='#8A6D00',ls='--')
arrow(0.10,0.33,0.76,0.12,'value that leaks away, never billed by the cloud',0.42,-0.115,col='#A33A3A',ls='--',rad=0.42)
ax.text(0.875,0.36,'compared with the yearly\nCARRY $H_t$ (wear, running\ncosts, return on the money)',ha='center',va='top',fontsize=8,style='italic',color='#1E2761')
ax.set_title('Where an AI customer dollar goes',fontsize=12,fontweight='bold',color='#1E2761',pad=8)
plt.tight_layout(); plt.savefig('f18_flow.pdf'); plt.savefig('f18_flow.png',dpi=200)
