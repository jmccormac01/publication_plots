import sys
from matplotlib import rc
try:
    from matplotlib import cycler
except ImportError:
    print('Cannot find cycler within matplotlib. Old version?')
    print('Trying to import cycler manually')
    try:
        from cycler import cycler
    except ImportError:
        print('Cannot find cycler')
        print('Update matplotlib to v2+ or install cycler manaully')
        print('https://github.com/matplotlib/cycler')
        sys.exit(1)

# DATA GLOBALS
DATA_LINE_COLOR = 'k'
DATA_LINE_STYLE = '-'
DATA_LINE_WIDTH = 0.5
MODEL_LINE_COLOR = 'r'
MODEL_LINE_STYLE = '-'
MODEL_LINE_WIDTH = 0.7

# AXES GLOBALS
AXES_LINE_WIDTH = 0.5
AXES_MAJOR_TICK_LENGTH = 4
AXES_MINOR_TICK_LENGTH = AXES_MAJOR_TICK_LENGTH/2.
AXES_XTICK_DIRECTION = 'out'
AXES_YTICK_DIRECTION = 'in'

# FIGURE GLOBALS
ONE_COL_WIDTH = 3.46
TWO_COL_WIDTH = 7.09
DPI = 800

def general():
    """
    General settings for all plot types. Call this first,
    then call any cascading style required
    """
    rc('font', family='Times New Roman', size=7)
    rc('text', color='black', usetex=True)
    rc('figure', dpi=DPI)
    rc('axes',
       xmargin=0.05,
       ymargin=0.05,
       linewidth=AXES_LINE_WIDTH,
       labelsize=7,
       prop_cycle=cycler('color',['black']))
    rc('axes.formatter', limits=(-4, 4))
    rc('axes.spines', left=True, right=True)
    rc('xtick',
       labelsize=7,
       direction=AXES_XTICK_DIRECTION)
    rc('xtick.major',
       size=AXES_MAJOR_TICK_LENGTH,
       width=AXES_LINE_WIDTH)
    rc('xtick.minor',
       visible=True,
       size=AXES_MINOR_TICK_LENGTH,
       width=AXES_LINE_WIDTH)
    rc('ytick',
       labelsize=7,
       direction=AXES_YTICK_DIRECTION)
    rc('ytick.major',
       size=AXES_MAJOR_TICK_LENGTH,
       width=AXES_LINE_WIDTH)
    rc('ytick.minor',
       visible=True,
       size=AXES_MINOR_TICK_LENGTH,
       width=AXES_LINE_WIDTH)

def one_by_one():
    """
    One-column-width plot settings
    """
    rc('figure', figsize=(ONE_COL_WIDTH, ONE_COL_WIDTH))

def two_by_one():
    """
    One-column-width by two-column-width plot
    """
    rc('figure', figsize=(TWO_COL_WIDTH, ONE_COL_WIDTH))

def two_by_two():
    """
    Two-column-width plot settings
    """
    rc('figure', figsize=(TWO_COL_WIDTH, TWO_COL_WIDTH))

def one_by_two():
    """
    Two-column-width plot settings
    """
    rc('figure', figsize=(TWO_COL_WIDTH, ONE_COL_WIDTH))
