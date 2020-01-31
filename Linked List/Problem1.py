# Problem 1: How do you find the middle element 
#            of a singly linked list in one pass?

#Approach: Taking two pointers as head, I will iterate 
#          both. One will enter the next node at every 
#          iteration and the other head will enter the 
#          next node at every two iteration. In this way,
#          the second head will be at the middle when
#          the first head reaches the end.
 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




