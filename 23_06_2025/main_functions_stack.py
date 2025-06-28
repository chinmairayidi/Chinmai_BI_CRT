class stack:
    def pop(self):
        if self.isempty():
            print("stack is empty")
    def peek(self):
        Len = len(self.stack)
        print(f"peek element is {self.stack[Len-1]}")
    def Display(self):
        for i in self.stack:
            print(i)
stack = stack
stack.pop()
stack.peek()
stack.Display()


