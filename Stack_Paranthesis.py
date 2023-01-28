"""Problem statement 1: check if Paranthesis in a string are balanced
    -> Balanced: (), {}{}, (({[]}))
    -> Not Balanced: ((), {{{}}], [][]]]
    
    *edge case 1: (()
    *edge case 2: }}"""

#SOLUTION:

"""Condition: opening brackets == closing brackets"""

from Stack_ds import Stack


#a function which checks the commented condition opening bracket == closing bracket

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '{' and p2 == '}':
        return True
    if p1 == '[' and p2 == ']':
        return True
    else: 
        return False

#a function that iterates over an input string and checks if its balanced or not.

def paren_str_balanced(paren_str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_str) and is_balanced:
        paren = paren_str[index] #slice off the elements of the string according to index

        if paren in '({[': #check if paren has any of the opening brackets

            s.push(paren) #if yes == push it into a stack

        else: 
            if s.is_empty():
                is_balanced = False 
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index+=1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(paren_str_balanced(""))