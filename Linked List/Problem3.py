#Problem 3: How do you reverse a linked list?

#Approach: Using recursion


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insertAtTail(self, newNode, headNode):
        if headNode is None:
            self.head = newNode
            return
        
        while headNode.next is not None:
            headNode = headNode.next
        
        headNode.next = newNode


    def reverseList(self, curNode):
        if curNode.next is None:
            self.head = curNode
            return
        
        self.reverseList(curNode.next)
        curNode.next.next = curNode
        curNode.next = None


    def printList(self, headNode):
        while headNode is not None:
            print(headNode.data)
            headNode = headNode.next
        

linkedList = LinkedList()

newNode = Node("asif")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("helal")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("anas")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("ashik")
linkedList.insertAtTail(newNode, linkedList.head)

linkedList.printList(linkedList.head)
print("##################")
linkedList.reverseList(linkedList.head)
linkedList.printList(linkedList.head)