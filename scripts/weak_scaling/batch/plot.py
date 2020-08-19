import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import myutils.mpl


# FINS_BATCH = ???
# FINS_2PP = ???

FOUT_PDF = "../../figures/weak_scaling/figure.pdf"
FOUT_PGF = "../../figures/weak_scaling/figure.pgf"

FIG_WIDTH = 0.45 * 681.159  # in pts


def parse_file(fname):
    print(fname)
    with open(fname) as f:
        s = f.read()

    match1 = re.search("running with (\d+) MPI process", s)
    match2 = re.search("Total wallclock time elapsed since start\s+\|\s+(\S+)s", s)

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

xs = []
ys = []
for nproc in range(1, 13):
    x,y = parse_file("out/batch{}.txt".format(nproc))
    xs.append(x)
    ys.append(y)
ax.plot(xs, ys, label="Particle property")

xs = []
ys = []
for nproc in range(1, 13):
    x,y = parse_file("out/2pp{}.txt".format(nproc))
    xs.append(x)
    ys.append(y)
ax.plot(xs, ys, label="Material model")

ax.set_xlabel("Number of processors")
ax.set_ylabel("Runtime (s)")
ax.legend(frameon=False)

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")


