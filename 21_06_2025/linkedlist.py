class node:
    def __init__(self,data):
        self.data =data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_front(self,data):
        new =node(data)
        new.next=self.head
        self.head=new
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end="--->")
            temp = temp.next
        print("none")
L=linkedlist()
L.insert_front(5)
L.insert_front(15)
L.insert_frint(20)
L.show()