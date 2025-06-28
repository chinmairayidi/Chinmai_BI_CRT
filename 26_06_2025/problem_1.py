'''
You're given a dataset containing gene expression levels across 
multiple timepoints.Your task is to:
Read the dataset
Calculate variance of expression per gene
Identify the top N most dynamic genes
Plot their expression profile using matplotlib
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("expression_data.csv")
gene_ids = df["Gene_ID"]
expression_data = df.drop(columns=["Gene_ID"])
variances = expression_data.var(axis=1)
N = 3
top_indices = np.argsort(-variances)[:N] 
top_genes = gene_ids.iloc[top_indices]
top_expr = expression_data.iloc[top_indices]
timepoints = expression_data.columns.tolist()
plt.figure(figsize=(10, 6))
for i in range(N):
    plt.plot(timepoints, top_expr.iloc[i], marker='o', label=top_genes.iloc[i])
plt.title(f"Top {N} Most Dynamic Genes (by Variance)")
plt.xlabel("Timepoints")
plt.ylabel("Expression Level")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()