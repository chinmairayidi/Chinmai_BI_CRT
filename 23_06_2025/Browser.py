'''
# write a python program to stimulate the behaviour of a web page or web browsers back button when a user visits a new page push it to the stack 
  when the user clicks back pop the top page and go back to the previous page

'''
class Browser:
    def __init__(self):
        self.history=[]
    def visit(self,page):
        self.history.append(page)
        print(f"visited {page}")
    def Undo(self):
        if len(self.history)>1:
            self.history.pop
            print(f"back to prevois page,{self.history[-1]}")
        else:
            print("no pages to comeback")
browser = Browser()
browser.visit('https//google.com')
browser.visit('https//linkdin.com')
browser.visit('https//github.com')
browser.Undo()
browser.Undo()
browser.Undo()


