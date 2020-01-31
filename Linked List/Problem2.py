#Problem 2: How do you check if a given linked list contains a cycle? 
#           How do you find the starting node of the cycle?

#Approach: Taking two pointers as head, I will iterate 
#          both. One will enter the next node at every 
#          iteration and the other head will enter the 
#          next node at every two iteration. If the two
#          head are same at any point then there is a 
#          cycle. Otherwise if the first head reaches None
#          then there is no cycle in the linked list


