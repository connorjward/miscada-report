import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import myutils.mpl


FIN = "../data/decompression_batch/particles.csv"
FOUT_PDF = "../figures/decompression_batch.pdf"
FOUT_PGF = "../figures/decompression_batch.pgf"
FIG_WIDTH = 0.45 * 681.159  # in pts

CNAMES = ["CaO","FeO","MgO","SiO2"]


mpl.use('pgf')  # this disables plt.show()
mpl.rcParams.update({'font.family': 'serif',
    'text.usetex': True,
    'axes.labelsize': 8,
    'font.size': 8,
    'legend.fontsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8 })

df = pd.read_csv(FIN)

fig = plt.figure(dpi=200, figsize=myutils.mpl.figsize_from_width(FIG_WIDTH))
ax1 = fig.add_axes((0.1, 0.5, 0.8, 0.4))
ax2 = fig.add_axes((0.1, 0.1, 0.8, 0.3), sharex=ax1)

# Remove the last point where the particle vanishes.
df = df[:-1]

for cname in CNAMES:
    ax1.plot(
        "Time",
        "avg(liquid composition {})".format(cname), 
        data=df,
        label=cname
    )
ax1.legend(frameon=False)
ax1.set_ylabel("Melt composition (mol)")

ax2.plot("Time", "avg(liquid n moles)", data=df)
ax2.set_xlabel("Time (yr)")
ax2.set_ylabel("Melt amount (mol)")

plt.savefig(FOUT_PDF, bbox_inches="tight")
plt.savefig(FOUT_PGF, bbox_inches="tight")

