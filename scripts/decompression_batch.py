import sys

import matplotlib.pyplot as plt
import pandas as pd


fname = sys.argv[1]

df = pd.read_csv(fname)

fig,ax = plt.subplots()
for cname in ["CaO","FeO","MgO","SiO2"]:
    ax.plot(
        "Time", 
        "avg(composition liquid {})".format(cname), 
        data=df,
        label=cname
    )

ax2 = ax.twinx()
ax2.plot("Time", "avg(n moles liquid)", data=df)


fig.legend()

plt.show()
