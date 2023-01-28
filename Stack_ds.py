"""Implementation of Stack: data structure in Python"""


class Stack:

    def __init__(self):  #constructor for our class
        self.items = [] #an empty list which will help in implementation of stack

    def push(self, item):   #a function which defines the push character of a stack
        self.items.append(item)   
        """append also appends the element into the list just like a stack"""

    def pop(self):   #function for popping out the top element
        return self.items.pop()

    def is_empty(self):
        return self.items == []     #it returns a boolean value(True/False), if stack is empty

    def peek(self):
        if not self.is_empty(): #if stack is not empty 
            return self.items[-1] #accessing the last element/top element


    def return_stack(self):
        return self.items

"""stack = Stack()
print(stack.is_empty())
stack.push("A")

stack.push("B")

stack.push("C")

stack.push("D")

print(stack.return_stack())
print(stack.peek())
print(stack.is_empty())"""