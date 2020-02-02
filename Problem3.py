#Problem 3: Infix to Postfix



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
        self.top = self.top.next


    def stackTop(self):
        if self.stackEmpty(): return False
        return self.top.data
            

    def stackEmpty(self):
        if self.top is None:
            return True
        return False

operatorWeight = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

openParentheses = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}

def isOperator(oper):
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        return True
    return False


def isOperand(oper):
    if oper >= '0' and oper <= '9': return True
    if oper >= 'a' and oper <= 'z': return True
    if oper >= 'A' and oper <='Z': return True
    return False


def isOpenPar(par):
    if par == '(' or par == '{' or par == '[':
        return True
    return False


def isClosePar(par):
    if par == ')' or par == '}' or par == ']':
        return True
    return False


def highPrec(op1, op2):
    if operatorWeight[op1] >= operatorWeight[op2]:
        return True
    return False


stack = Stack()

inString = input("Enter Your Infix String:\n")
postString = ""


for char in inString:
    if isOperand(char): postString += char
    if isOpenPar(char): stack.stackPush(char)
    if isOperator(char):
        if stack.stackEmpty(): 
            stack.stackPush(char)
            continue
        if isOperator(stack.stackTop()):
            if highPrec(stack.stackTop(), char):
                while isOperator(stack.stackTop()): 
                    postString += stack.stackTop()
                    stack.stackPop()
        stack.stackPush(char)
    if isClosePar(char):
        while stack.stackTop() is not openParentheses[char]:
            postString += stack.stackTop()
            stack.stackPop()
            
        stack.stackPop()



while stack.stackTop():
    postString += stack.stackTop()
    stack.stackPop()

print(postString)
        
        






