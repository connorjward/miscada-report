import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import myutils.mpl


DATA_DIR = "../../../var/strong_scaling/particle_property/"
FIG_DIR = "../../../figures/strong_scaling/"

FIN_TEST = [DATA_DIR + "test{}.txt".format(n) for n in range(1, 13)]
FIN_CTRL = [DATA_DIR + "ctrl{}.txt".format(n) for n in range(1, 13)]

FOUT_PDF = FIG_DIR + "particle_property.pdf"
FOUT_PGF = FIG_DIR + "particle_property.pgf"

FIG_WIDTH = 0.49 * 416.13188  # in pts


def speedup(f, p):
    return 1 / (f + (1-f)/p)


def parse_file(fname):
    with open(fname) as f:
        s = f.read()

    match1 = re.search("running with (\d+) MPI process", s)
    match2 = re.search("Total wallclock time elapsed since start"
                       "\s+\|\s+(\S+)s", s)

    nproc = int(match1.group(1))
    time = float(match2.group(1))
        
    return nproc,time


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

xs = np.empty(12)
ys = np.empty(12)
for i,fname in enumerate(FIN_TEST):
    xs[i],ys[i] = parse_file(fname)
ax.plot(xs, ys[0]/ys, label="With Perple\_X")

xs = np.empty(12)
ys = np.empty(12)
for i,fname in enumerate(FIN_CTRL):
    xs[i],ys[i] = parse_file(fname)
ax.plot(xs, ys[0]/ys, label="Without Perple\_X")

xs = np.arange(1, 13)
ax.plot(xs, speedup(0.01, xs), label="_nolegend", linestyle="--", 
        linewidth=0.5, color="black")
ax.annotate("$f=0.01$", 
            (xs[6], speedup(0.01, ys[6])), 
            xytext=(7,-7),
            textcoords="offset points")

ax.plot(xs, speedup(0.1, xs), label="_nolegend", linestyle="--", 
        linewidth=0.5, color="black")
ax.annotate("$f=0.1", (xs[6], speedup(0.1, xs[6])),
            xytext=(7,-7),
            textcoords="offset points")

ax.plot(xs, speedup(0.5, xs), label="_nolegend", linestyle="--", 
        linewidth=0.5, color="black")
ax.annotate("$f=0.5$", (xs[6], speedup(0.5, xs[6])),
            xytext=(7,-9),
            textcoords="offset points")


ax.set_xlabel("Number of processors")
ax.set_ylabel("Speedup")
ax.legend(frameon=False)
ax.set_xticks(range(1, 13))

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")

