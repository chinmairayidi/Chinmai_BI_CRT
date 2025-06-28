# check for balanced parantheses
def is_balanced(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    match = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return len(stack) == 0
expr = input("Enter an expression: ")
if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
