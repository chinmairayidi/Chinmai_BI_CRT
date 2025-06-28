'''given protein sequencees,compute the ammino acid composition and display it as a pie chart'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data ={
    "protein id":[f"P{i}"for i in range (1,13)],
    "sequence":[
        "MKVIFLILALVTLVFS", "AGAGAGAGAG", "MTMDKSELVQKA", "AAAAAACCCCCCGGGGG",
        "MTEITAAMVKELRESTGAGM", "MNPLLILTFVAAALAAP", "GGLFGKGGVGK", "PAAPPAPPPP", 
        "GLSDGEWQLVL", "LSPADKTNVK", "MGDVEKGKKIF", "ADLGAVYVSR"
    ]
}
df = pd.DataFrame(data)
all_seq= "".join(df["sequence"])
count = Counter(all_seq)
labels,sizes =zip(*sorted(count.items()))

cmap = plt.colormaps.get_cmap("tab20")
colors = [cmap(i) for i in range(len(labels))]

plt.figure(figsize=(9, 9))
wedges, _, autotexts =plt.pie(
sizes,
labels = labels,
colors=colors,
explode=[0.5]*len(labels),
startangle=140,
autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*sum(sizes))})",
textprops=dict(color="black",fontsize=10)
)
plt.legend(
    wedges,
    [f"{aa}:{cnt}" for aa,cnt in count.items()],
    title="Amino Acid Composition",
    bbox_to_anchor=(1, 0.5),
    loc ="center left",
    fontsize=9
)
plt.title("ammino acid composition from 12 proteins",
          fontsize = 14,fontweight="bold",color="darkblue")
plt.tight_layout()
plt.show()
