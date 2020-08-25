import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import myutils.mpl


DATA_DIR = "../../../var/load_balancing/material_model/"
FIG_DIR = "../../../figures/load_balancing/"

FIN = DATA_DIR + "test.txt"

FOUT_PDF = FIG_DIR + "material_model.pdf"
FOUT_PGF = FIG_DIR + "material_model.pgf"

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
ys = ((df["Maximal cells per process"] 
     - df["Minimal cells per process"])
     / df["Average cells per process"])
ax.plot(xs, ys)

ax.set_xlabel("Time (years)")
ax.set_ylabel("Normalised range")

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")

