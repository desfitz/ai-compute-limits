"""Shared colour style for the paper's figures (v28): the deck's palette, no grey curves."""
import matplotlib as mpl
from cycler import cycler
PAL=['#1E2761','#2E86AB','#C0504D','#E08E45','#3BA272','#8E7CC3','#D4A72C','#5B9BD5']
mpl.rcParams.update({'axes.prop_cycle':cycler(color=PAL),'axes.edgecolor':'#33415C','axes.labelcolor':'#1E2761',
 'xtick.color':'#33415C','ytick.color':'#33415C','axes.titlecolor':'#1E2761','axes.titleweight':'bold','grid.color':'#DCE3EE','legend.frameon':False})
PC={'Plateau':'#1E2761','ArmsRace':'#C0504D','Rationalize':'#3BA272','_adapt':'#E08E45','Adaptive':'#E08E45'}
