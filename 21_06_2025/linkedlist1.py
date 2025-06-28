#create a node and print its values
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node= Node(10)
print(node.data)
node1=Node(20)
print(node.data)
node2=Node(30)
print(node.data)
current=node
current.next=node1
node1.next=node2
while current:
    print(current.data,end="-->")
    current=current.next
print("none")