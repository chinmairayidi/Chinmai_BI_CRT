from collections import deque
stack = deque()
stack.append('A')
stack.append('b')
stack.append('c')
print("stack after enqueuing:",stack)
top = stack.pop()
print("popped element",top)
print("stack after popping",stack)
if not stack:
    print("stack is empty")
else:
    print("stack is not empty")
print("top element",stack[-1])