class Stack():
    def __init__(self): # Corrected the constructor name
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} is added to stack")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.Stack.pop()
            print("element is removed")
    def peek(self):
        Len=len(self.Stack)
        print(f"peek element is{self.Stack[Len-1]}")
    def Display(self):
        self.Stack.reverse()
        for i in self.Stack:
            print(i)
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print("initial stack contain elements of:")
stack.Display()
stack.pop()
stack.peek()
stack.Display()
