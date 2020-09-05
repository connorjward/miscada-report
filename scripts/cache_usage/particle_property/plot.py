import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import myutils.mpl

DATA_DIR = "../../../var/cache_usage/particle_property/"
FIG_DIR = "../../../figures/cache_usage/"

CACHE_TOLS = ["1e-{}".format(n) for n in range(2, 6)]

FOUT_PDF = "../../../figures/cache_usage/particle_property.pdf"
FOUT_PGF = "../../../figures/cache_usage/particle_property.pgf"

FIG_WIDTH = 0.49 * 416.13188  # in pts
FIG_HEIGHT = FIG_WIDTH*1.4
FIG_SIZE = myutils.mpl.figsize_from_width(FIG_WIDTH, FIG_HEIGHT)

def parse_file(fname):
    with open(fname) as f:
        cols = re.findall("# \d+: (.*)", f.read())
        
    return pd.read_table(fname, names=cols, comment="#", delim_whitespace=True)


mpl.use('pgf')  # this disables plt.show()
mpl.rcParams.update({
    'font.family': 'serif', 
    'text.usetex': True,
    'axes.labelsize': 8, 'font.size': 8,
    'legend.fontsize': 7,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8 
})

fig = plt.figure(figsize=FIG_SIZE, dpi=200)
ax1 = fig.add_axes((0.1,0.35,0.8,0.6))
ax2 = fig.add_axes((0.1,0.1,0.8,0.25), sharex=ax1)

for tol in CACHE_TOLS:
    df = parse_file(DATA_DIR + "{}.txt".format(tol))
    ax1.plot(df["Time (years)"]/1e6, df["Cache hit rate"]*100, 
             label="{}%".format(float(tol)*100))

df = parse_file(DATA_DIR + "{}.txt".format(CACHE_TOLS[0]))
ts = df["Time (years)"].to_numpy()
ax2.plot(ts[:-1]/1e6, (ts[1:]-ts[:-1])/1e3)

ax1.set_ylabel("Hit rate (%)")
ax1.legend(frameon=False, loc="center")
ax1.set_yticks(np.arange(0, 100+20, 20))

ax2.set_xlabel(r"Time ($\times 10^6 \, \mathrm{yr}$)")
ax2.set_ylabel(r"Timestep ($\times 10^3 \, \mathrm{yr}$)")

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")


