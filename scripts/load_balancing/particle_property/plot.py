import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import myutils.mpl


DATA_DIR = "../../../var/load_balancing/particle_property/"
FIG_DIR = "../../../figures/load_balancing/"

FIN = DATA_DIR + "test.txt"

FOUT_PDF = FIG_DIR + "particle_property.pdf"
FOUT_PGF = FIG_DIR + "particle_property.pgf"

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
ax.plot(df["Time (years)"]/1e6, 
        df["Average particles per process"],
        label="Average")
ax.fill_between(df["Time (years)"]/1e6, 
                df["Minimal particles per process"], 
                df["Maximal particles per process"],
                label="Range",
                alpha=0.3)

ax.set_xlabel(r"Time ($\times 10^6 \, \mathrm{yr}$)")
ax.set_ylabel("Number of particles")
ax.legend(frameon=False, loc="upper left")
ax.set_xlim(0, 1.5)

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")

