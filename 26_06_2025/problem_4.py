# write a python program to count how many genes belong to each family from the given data and visualize it using barchart
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}
df = pd.DataFrame(data)
family_count = df['Family'].value_counts()
plt.figure(figsize=(8, 5))
family_count.plot(kind='bar', color='yellow', edgecolor='blue')
plt.title("Number of Genes in a  Family")
plt.xlabel("Gene Family")
plt.ylabel("Count")
plt.tight_layout()
plt.show()