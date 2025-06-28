'''
Given dna sequence,calculate the gc content of each and plot it as a histogram
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
data = {
    "GeneID": [f"G{i}" for i in range(1, 16)],
    "Sequence": [
        "ATGCGTAA", "GGGCGCGT", "ATATATAT", "CGCGATAT",
        "GCGTGCAT", "TTATTATA", "CCGGCCGG", "GATCGATC",
        "TATATATA", "GCGCGCGC", "ATGCATGC", "GGATCCGG",
        "CATCATGG", "TGCATGCA", "GGTACCGA"
    ]
}
df = pd.DataFrame(data)
def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count/len(seq)) * 100
df['GC_Content'] = df['Sequence'].apply(gc_content)
plt.figure(figsize=(10, 6))
plt.hist(df['GC_Content'], bins=10, color='black', edgecolor='red')
plt.title("-----GC_Content----")
plt.xlabel("GC Content")
plt.ylabel("Number of Sequences")
plt.grid(True)
plt.tight_layout()
plt.show()