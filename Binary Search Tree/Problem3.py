#Problem 3: Is BST?

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.comp = None
        self.test = True

    def insertData(self, data, tempRoot):
        if tempRoot is None: self.root = Node(data)
        elif (data > tempRoot.data):
            if tempRoot.right is None:
                tempRoot.right = Node(data)
            else:
                self.insertData(data, tempRoot.right)
        else:
            if tempRoot.left is None:
                tempRoot.left = Node(data)
            else:
                self.insertData(data, tempRoot.left)
    

    def isBST(self, tempRoot):
        if tempRoot is None: return self.test
        if self.test: 
            self.isBST(tempRoot.left)
            if self.comp is None or self.comp <= tempRoot.data: 
                self.comp = tempRoot.data
            else:
                self.test = False
            self.isBST(tempRoot.right)
        return self.test