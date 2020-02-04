#Inorder Successor

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
        elif data > tempRoot.data:
            if tempRoot.right is None:
                tempRoot.right = Node(data)
            else:
                self.insertData(data, tempRoot.right)
        else:
            if tempRoot.left is None:
                tempRoot.left = Node(data)
            else:
                self.insertData(data, tempRoot.left)

    
    def inSuc(self):


orchid = BST()

orchid.insertData('F', orchid.root)
orchid.insertData('D', orchid.root)
orchid.insertData('J', orchid.root)
orchid.insertData('B', orchid.root)
orchid.insertData('A', orchid.root)
orchid.insertData('E', orchid.root)
orchid.insertData('K', orchid.root)
orchid.insertData('G', orchid.root)
orchid.insertData('C', orchid.root)
orchid.insertData('I', orchid.root)