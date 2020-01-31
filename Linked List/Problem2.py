#Problem 2: How do you check if a given linked list contains a cycle? 
#           How do you find the starting node of the cycle?

#Approach: Taking two pointers as head, I will iterate 
#          both. One will enter the next node at every 
#          iteration and the other head will enter the 
#          next node at every two iteration. If the two
#          head are same at any point then there is a 
#          cycle. Otherwise if the first head reaches None
#          then there is no cycle in the linked list


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


    def hasCycle(self, head1, head2):
        count = 1
        while head1.next is not None:
            head1 = head1.next
            if (count%2) is 0: 
                head2 = head2.next
            if(head1 == head2):
                print("Cycle present")
                return
            count += 1
        
        print("Cycle absent")


    def printList(self, headNode):
        while headNode is not None:
            print(headNode.data)
            headNode = headNode.next
        

linkedList = LinkedList()
newNode = Node("asif")
linkedList.insertAtTail(newNode, linkedList.head)
cycleNode = Node("helal")
linkedList.insertAtTail(cycleNode, linkedList.head)
newNode = Node("anas")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("ashik")
linkedList.insertAtTail(newNode, linkedList.head)
newNode = Node("sabbir")
linkedList.insertAtTail(newNode, linkedList.head)

linkedList.insertAtTail(cycleNode, linkedList.head)



linkedList.hasCycle(linkedList.head, linkedList.head)