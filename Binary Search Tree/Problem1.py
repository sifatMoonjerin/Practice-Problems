#Problem 1: Find min and max element in BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


    def insertData(self, data, tempRoot):
        if self.root is None:
            self.root = Node(data)
            
        else:
            if tempRoot is None:
                tempRoot = Node(data)
            elif data > tempRoot.data:
                tempRoot.right = self.insertData(data, tempRoot.right)
            else:
                tempRoot.left = self.insertData(data, tempRoot.left)
            return tempRoot
    

    def findMin(self, root):
        if root is None:
            print("Empty Tree")
            return
        elif root.left is None:
            return root.data
        else:
            return self.findMin(root.left)


orchid = BST()
orchid.insertData(15, orchid.root)
orchid.insertData(10, orchid.root)
orchid.insertData(20, orchid.root)
orchid.insertData(25, orchid.root)
orchid.insertData(8, orchid.root)
orchid.insertData(12, orchid.root)
minimum = orchid.findMin(orchid.root)
print(minimum)



