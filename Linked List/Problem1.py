# Problem 1: How do you find the middle element 
#            of a singly linked list in one pass?

#Approach: Taking two pointers as head, I will iterate 
#          both. One will enter the next node at every 
#          iteration and the other head will enter the 
#          next node at every two iteration. In this way,
#          the second head will be at the middle when
#          the first head reaches the end. (ignoring empty list)
 

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


    def middleElement(self, head1, head2):
        count = 1
        while head1.next is not None:
            head1 = head1.next
            if (count%2) is 0: head2 = head2.next
            count += 1
        print(head2.data)


    def printList(self, headNode):
        while headNode is not None:
            print(headNode.data)
            headNode = headNode.next
        

linkedList = LinkedList()


#Enter list nodes...
for i in range(5):
    newNode = Node(input("Enter data: "))
    linkedList.insertAtTail(newNode, linkedList.head)
    

linkedList.printList(linkedList.head)
print("######################")
linkedList.middleElement(linkedList.head, linkedList.head)