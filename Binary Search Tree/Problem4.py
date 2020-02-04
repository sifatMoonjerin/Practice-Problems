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


    def findData(self, data, tempRoot):
        if tempRoot is None: return tempRoot
        elif data == tempRoot.data: return tempRoot
        elif data > tempRoot.data:
            return self.findData(data, tempRoot.right)
        else:
            return self.findData(data, tempRoot.left)


    def findMin(self, tempRoot):
        while tempRoot.left is not None:
            tempRoot = tempRoot.left
        return tempRoot.data

    
    def inSuc(self, data, tempRoot):
        current = self.findData(data, tempRoot)
        if current is None: return None
        elif current.right is not None:
            return self.findMin(current.right)
        else:
            ancestor = tempRoot
            successor = None
            while ancestor is not current:
                if ancestor.data > current.data:
                    successor = ancestor.data
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor




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

print(orchid.inSuc('K', orchid.root))