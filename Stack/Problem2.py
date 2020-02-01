#Problem 2: Balanced parentheses


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


    def stackPush(self,data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode


    def stackPop(self):
        if self.stackEmpty(): return False
        data = self.top.data
        self.top = self.top.next
        return data


    def stackTop(self):
        return self.top.data
            

    def stackEmpty(self):
        if self.top is None:
            return True
        return False


stack = Stack()


def balancedParentheses(str):
    closePar = {
        ']' : '[',
        '}' : '{',
        ')' : '('
    }
    for char in str:
        if char == '[' or char == '{' or char == '(':
            stack.stackPush(char)
            continue

        if char == ']' or char == '}' or char == ')':
            check = stack.stackPop()
            if check != closePar[char]: return False
        
    return stack.stackEmpty()



string = input("Enter a test string: ")
result = balancedParentheses(string)
if result: print('Yap! Balanced Parentheses!')
else: print('Nay!!!') 
