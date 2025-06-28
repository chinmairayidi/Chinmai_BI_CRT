#Node class single linkedlist 
class Node():
    def __init__(self,data):
        self.Data=data
        self.Next=None
First=Node(10)
Second=Node(20)
Third=Node(30)
Fourth=Node(40)
Fifth=Node(50)
head=First
head.Next=Second
Second.Next=Third
Third.Next=Fourth
Fourth.Next=Fifth
Current=head
while Current:
    print(Current.Data,end=" -> ")
    Current = Current.Next
print("None")