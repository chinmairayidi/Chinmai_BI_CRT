class Queues:
    def __init__(self):
        self.item = []
#adds item to rear(end)
    def enqueue(self,item):
        self.item.append(item)
#checks queue is empty or not
    def is_empty(self):
        return len(self.item) == 0
#checks and returns the front item
    def dequeue(self):
        if self.is_empty():
            return None
        return self.item.pop(0)
    def peek_front(self):
        if self.is_empty():
            return None
        return self.item[0]
#looks at the rear item without removing
    def peek_rare(self):
        if self.is_empty():
            return None
        return self.item[-1]
    def size(self):
        return len(self.item)
# Creating an instance of Queues
q = Queues()
# Adding items to the queue
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
# Displaying the size of the queue
print("Queue Size:", q.size())  
# Checking the front and rear items
print("Front item:", q.peek_front())
print("Rear item:", q.peek_rare())
# Removing items from the queue
print("Dequeued item:", q.dequeue()) 
# Checking again after dequeue
print("Front item after dequeue:", q.peek_front()) 
print("Rear item after dequeue:", q.peek_rare())
# Final size
print("Queue Size:", q.size())
# Check if queue is empty
print("Is queue empty?", q.is_empty())

