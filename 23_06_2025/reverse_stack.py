class Stack():
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} id added to stack")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.Stack.pop()
            print("element is removed")
    def length(self):
        l=len(self.Stack)
        print(f"Length of the stack is: {l}")
    def Display(self):
        self.Stack.reverse()
        Str=[]
        for i in self.Stack:
            Str.append(i)
        Rev_Str="".join(Str)
        print(Rev_Str)
stack=Stack()
stack.push("S")
stack.push("R")
stack.push("A")
stack.push("V")
stack.push("Y")
stack.push("A")
print("initial stack contain elements of:")
stack.Display()
stack.length()