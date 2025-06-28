#Create Some Nodes in a LL and Print their Values.
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None        
    def AddNode(self,data):
        N_Node=Node(data)
        N_Node.next=self.head
        self.head=N_Node
    def Display_List(self):
        current=self.head
        while current:
            print(current.Data,end="-->")
            current=current.next
        print("None")    
L1=LinkedList()
L1.AddNode(25.89)
L1.AddNode(99.56)
L1.AddNode(76.54)
L1.AddNode(100)
L1.Display_List()