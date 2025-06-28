from collections import deque
queue = deque()
queue.append('A')
queue.append('b')
queue.append('c')
print("Queue after enqueuing:",queue)
first = queue.popleft()
print("dequeuedd element",first)
print("queue after dequeuing",queue)
if not queue:
    print("queue is empty")
else:
    print("queue is not empty")
print("Front element",queue[0])






