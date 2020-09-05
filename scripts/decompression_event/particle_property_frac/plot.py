import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import myutils.mpl


DATA_DIR = "../../../var/decompression_event/particle_property_frac/"
FIG_DIR = "../../../figures/decompression_event/"

FIN = DATA_DIR + "particles.csv"
FOUT_PDF = FIG_DIR + "particle_property_frac.pdf"
FOUT_PGF = FIG_DIR + "particle_property_frac.pgf"

FIG_WIDTH = 0.49 * 416.13188  # in pts

CNAMES = ["CaO","FeO","MgO","SiO2"]
COLUMNS = ["avg(extracted melt composition {})".format(cname) for cname in CNAMES]


mpl.use('pgf')  # this disables plt.show()
mpl.rcParams.update({'font.family': 'serif',
    'text.usetex': True,
    'axes.labelsize': 8,
    'font.size': 8,
    'legend.fontsize': 7,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8 })

df = pd.read_csv(FIN)

fig,ax = plt.subplots(dpi=200, figsize=myutils.mpl.figsize_from_width(FIG_WIDTH))

# First plot the melt amount.
ax.plot(df["Time"]/1e3, df["avg(extracted melt n moles)"],
        color="black", label="_nolegend_")

xs = []
yss = []
for i,row in df.iterrows():
    x = row["Time"]

    if sum(row[COLUMNS]) > 0:
        ys = (row[COLUMNS] / sum(row[COLUMNS]) 
             * row["avg(extracted melt n moles)"])
    else:
        ys = [0.0 for _ in row[COLUMNS]]

    xs.append(x)
    yss.append(ys)

ax.stackplot(np.array(xs)/1e3, np.array(yss).swapaxes(0, 1), labels=CNAMES)

ax.legend(frameon=False)
ax.set_xlabel(r"Time ($\times 10^3 \, \mathrm{yr}$)")
ax.set_ylabel("Melt volume (%)")
ax.set_xlim(40, 100)
ax.set_ylim(0, 5.3)

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")

