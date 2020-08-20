import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import myutils.mpl


CACHE_TOLS = ["1e-{}".format(n) for n in range(2, 6)]

FOUT_PDF = "../../../figures/cache_usage/material_model.pdf"
FOUT_PGF = "../../../figures/cache_usage/material_model.pgf"

FIG_WIDTH = 0.45 * 681.159  # in pts


def parse_file(fname):
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

for tol in CACHE_TOLS:
    df = parse_file("data/{}.txt".format(tol))
    xs = df["Time (years)"]
    ys = df["Cache hit rate"]

    ax.plot(xs, ys, label=tol)

ax.set_xlabel("Time (years)")
ax.set_ylabel("Hit rate")
ax.legend(frameon=False)

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")


