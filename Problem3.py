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
        data = self.top.data
        self.top = self.top.next
        return data


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

def highPrec(op1, op2):
    if operatorWeight[op1] > operatorWeight[op2]:
        return True
    return False


