'''write a python program to take the length of queue as input from the user and add the elements
   by using enqueue method and print the elements present in the queue and remove the elements from 
   the queue and check wether the queue is empty or not  and print the front peek and rare peek.
'''
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    def is_empty(self):
        return len(self.items) == 0
    def front_peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    def rear_peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def display(self):
        return self.items
queue = Queue()
num = input("Enter no.of elements to add to the queue: ")
for i in range(num):
    element = input(f"Enter element {i+1}: ")
    queue.enqueue(element)
print("Elements in the queue:")
print(queue.display())
print("Dequeuing all elements:")
while not queue.is_empty():
    removed = queue.dequeue()
    print(f"Removed: {removed}")
if queue.is_empty():
    print("Queue is now empty.")
else:
    print("Queue is not empty.")
print(f"Front Peek: {queue.front_peek()}")
print(f"Rear Peek: {queue.rear_peek()}")
    