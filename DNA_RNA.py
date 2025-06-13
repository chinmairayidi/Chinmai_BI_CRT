DNA=input("Enter the DNA Sequence:")
RNA=""
for i in range(len(DNA)):
    if DNA[i] == 'T':
        RNA+='U'
    else:
        RNA+=DNA[i]
print(f"The RNS Sequence is :{RNA}")