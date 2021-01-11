from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0 
    
    def size(self):
        return len(self.container)

    

# Question 1: Write a function in python that can reverse a string using the stack data structure
def reverse_stack(mystring):
    stack = Stack()
    try:
        for x in mystring:
            stack.push(x)
    except:
        print("You can only iterate through strings!")

    output = ""
    try:
        while stack.size() != 0:
            output += str(stack.pop())
        print(output)
    except:
        print("This function only works with strings")

# Question 2: Write a function in python that checks if parentheses in the string are balanced

def is_match(ch1, ch2):
    match_dict = {
        ")": "("
        "}": "{"
        "]": "["
    }

    return matchdict[ch1] == ch2


def is_balanced(mystring):
    stack = Stack()
    for c in mystring:
        if c == "(" or c == "{" or c == "[":
            stack.push(c) # Sends the first half of the parenthesis into a stack
        
        elif c == ")" or c == "}" or c == "]":
            if stack.size() == 0:
                return False
            elif not is_match(ch, stack.pop()): # Checks against the stack that contains the first half of the parenthesis
                return False

            

    

stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

print(is_balanced("({a+b})"))
