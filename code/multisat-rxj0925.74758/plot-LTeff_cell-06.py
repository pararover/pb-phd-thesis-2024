import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, LogLocator, FormatStrFormatter, MaxNLocator, FuncFormatter

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Liberation Sans'

def log_formatter(x, pos):
    if x == 1:
        return '1'
    else:
        return f'$10^{{{int(np.log10(x))}}}$'