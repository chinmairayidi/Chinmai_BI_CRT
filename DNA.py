seq=input("Enter the DNA sequence: ")
A,T,G,C=0,0,0,0
for ch in seq:
    if ch=='A':
        A+=1
    elif ch=='T':
        T+=1
    elif ch=='G':
        G+=1
    else:
        C+=1
print("The count of A's :",A)
print("The count of T's :",T)
print("The count of G's :",G)
print("The count of C's :",C)
#
seq=input("Enter the DNA sequence: ")
base_count={'A':seq.count('A'),'T':seq.count('T'),'G':seq.count('G'),'C':seq.count('C')}
print(base_count)