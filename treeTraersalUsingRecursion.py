class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySerachTree:

    def __init__(self):
        self.root = None

    def insert(self,value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        else:
            currentNode = self.root
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = Node(value)
                    return self
                currentNode.left.insert(value)
            if value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = Node(value)
                    return self
                currentNode.right.insert(value)
        return self

    def search(self,value):
        if self.root is None:
            return False
        else:
            currentNode = self.root
            if value < currentNode.left:
                currentNode.left.search(value)
            elif value > currentNode.right:
                currentNode.right.search(value)
            elif value == currentNode.value:
                return currentNode
        return False





