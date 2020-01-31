#Problem5: Remove duplicates from an unsorted linked list

#Approach: Using two loops

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


    def removeDuplicate(self, curNode):
        while curNode.next is not None:
            checkNode = curNode
            while checkNode.next is not None:
                if(checkNode.next.data == curNode.data):
                    checkNode.next = checkNode.next.next
                else: 
                    checkNode = checkNode.next
                
            curNode = curNode.next



    def printList(self, headNode):
        while headNode is not None:
            print(headNode.data)
            headNode = headNode.next
        

linkedList = LinkedList()

newNode = Node("helal")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("asif")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("helal")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("helal")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("anas")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("ashik")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("helal")
linkedList.insertAtTail(newNode, linkedList.head)


linkedList.printList(linkedList.head)
linkedList.removeDuplicate(linkedList.head)
print("#######")
linkedList.printList(linkedList.head)
