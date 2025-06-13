seq1 = input("Enter seq1 ").split()
print("Sequence 1 :", seq1)
seq2 = input("Enter seq2: ").split()
print("Sequence 1 :", seq1)
for i in seq1:
    for ch in seq2:
        if i not in ch:
            print(i)
        