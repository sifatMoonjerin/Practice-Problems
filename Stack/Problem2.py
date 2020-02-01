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
        if self.stackEmpty(): return 
        self.top = self.top.next


    def stackTop(self):
        return self.top.data
            

    def stackEmpty(self):
        if self.top is None:
            return True
        return False