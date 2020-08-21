import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import myutils.mpl


FIN = "data/test.txt"
FIN_CTRL = "data/ctrl.txt"

FOUT_PDF = "../../../figures/load_balancing/particle_property.pdf"
FOUT_PGF = "../../../figures/load_balancing/particle_property.pgf"

FIG_WIDTH = 0.45 * 681.159  # in pts


def read_statistics(fname):
    with open(fname) as f:
        cols = re.findall("# \d+: (.*)", f.read())
        
    return pd.read_table(fname, names=cols, comment="#", delim_whitespace=True)


mpl.use('pgf')  # this disables plt.show()
mpl.rcParams.update({
    'font.family': 'serif', 
    'text.usetex': True,
    'axes.labelsize': 8, 'font.size': 8,
    'legend.fontsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8 
})

fig,ax = plt.subplots(figsize=myutils.mpl.figsize_from_width(FIG_WIDTH),
                      dpi=200)

df = read_statistics(FIN)
xs = df["Time (years)"]
ys = ((df["Maximal particles per process"] 
     - df["Minimal particles per process"])
     / df["Average particles per process"])
ax.plot(xs, ys, label="With Perple\_X")

df = read_statistics(FIN_CTRL)
xs = df["Time (years)"]
ys = ((df["Maximal particles per process"] 
     - df["Minimal particles per process"])
     / df["Average particles per process"])
ax.plot(xs, ys, label="Without Perple\_X")

ax.set_xlabel("Time (years)")
ax.set_ylabel("???")
ax.legend(frameon=False)

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")

