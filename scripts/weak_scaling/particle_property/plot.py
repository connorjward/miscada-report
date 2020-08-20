import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import myutils.mpl


FIN_TEST = ["data/test{}.txt".format(n) for n in range(1, 13)]
FIN_CTRL = ["data/ctrl{}.txt".format(n) for n in range(1, 13)]

FOUT_PDF = "../../../figures/weak_scaling/particle_property.pdf"
FOUT_PGF = "../../../figures/weak_scaling/particle_property.pgf"

FIG_WIDTH = 0.45 * 681.159  # in pts


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

ax.set_xlabel("Number of processors")
ax.set_ylabel("Speedup")
ax.legend(frameon=False)

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")

