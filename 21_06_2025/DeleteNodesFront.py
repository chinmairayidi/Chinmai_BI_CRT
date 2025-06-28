#Delete the first node
def delete_front(self):
    if self.head:
        self.head = self.head.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end for list creation
    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # Delete first node
    def delete_front(self):
        if self.head:
            self.head = self.head.next

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.print_list()  # 10 --> 20 --> 30 --> None

ll.delete_front()
ll.print_list()  # 20 --> 30 --> None

