class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Manually create linked list nodes
a = Node(10)
b = Node(20)
c = Node(30)

# Link nodes
a.next = b
b.next = c

# Traverse and print the linked list
temp = a
while temp:
    print(temp.data, end=" --> ")
    temp = temp.next
print("None")  # To indicate the end of the list
