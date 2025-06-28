class Node:
    def __init__(self,data):
        self.Data=data
        self.Next=None
n=int(input("Enter Size of LL: "))
head = tail = None
for i in range(n):
    temp = int(input(f"Enter The value of node {i+1}: "))
    newNode = Node(temp)
    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.Next = newNode
        tail = newNode

current = head
while current:
    print(current.Data,end=' -> ')
    current = current.Next
print("None")