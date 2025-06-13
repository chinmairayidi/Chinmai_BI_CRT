seq=input("Enter the DNA sequence:")
for nucleotide in seq:
    if nucleotide=='A':
        nucleotide.replace('T')
    elif nucleotide=='G':
        nucleotide.replace('C')
print(seq)