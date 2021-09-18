


class GeneralTree():
    def __init__(self, root):
        self.root = root
        self.children = []
    
    def addChild(self, obj):
        self.children.append(obj)




class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self
    
    # Faster method
    # def insert(self, value):
    #     currentNode = self 
    #     while True:
    #         if value < currentNode.value:
    #             if currentNode.left is None:
    #                 currentNode.left = BST(value)
    #                 break
    #             else:
    #                 currentNode = currentNode.left
            
    #         else:
    #             if currentNode.right is None:
    #                 currentNode.right = BST(value)
    #                 break
    #             else:
    #                 currentNode = currentNode.right
    #     return self

root = BST(10)
root.insert(5)
root.insert(5)
root.insert(4)
print(root.value, root.left.value)