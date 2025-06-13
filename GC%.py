DNA=input("Enter the DNA sequence:")
G,C=0,0
total_bases=len(DNA)
for i in range(len(DNA)):
    if DNA[i]=='G':
        G+=1
    elif DNA[i]=='C':
        C+=1
print(G+C)
GC=(G+C)/total_bases
GC_percentage=GC*100
print(f"The GC percentage is : {GC_percentage}")
if GC_percentage>60:
    print("High GC")
elif GC_percentage > 40 and GC_percentage < 60:
    print("Moderate GC")
elif GC_percentage<=40:
    print("Low GC")