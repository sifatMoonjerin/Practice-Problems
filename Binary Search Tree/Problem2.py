#Problem 2: Find the height of the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
class BST:
    def __init__(self):
        self.root = None

    
    def insertData(self, data, tempRoot):
        if tempRoot is None:
            self.root = Node(data)
            return
        elif(data > tempRoot.data):
            if tempRoot.right is None:
                tempRoot.right = Node(data)
            else:
                self.insertData(data, tempRoot.right)
        else:
            if tempRoot.left is None:
                tempRoot.left = Node(data)
            else:
                self.insertData(data, tempRoot.left)


    def treeHeight(self, tempRoot):
        if tempRoot is None: return -1
        return max(self.treeHeight(tempRoot.left), self.treeHeight(tempRoot.right)) + 1


orchid = BST()
orchid.insertData(15, orchid.root)
orchid.insertData(10, orchid.root)
orchid.insertData(20, orchid.root)
orchid.insertData(25, orchid.root)
orchid.insertData(8, orchid.root)
orchid.insertData(12, orchid.root)
orchid.insertData(18, orchid.root)
orchid.insertData(7, orchid.root)

height = orchid.treeHeight(orchid.root)
print(height)