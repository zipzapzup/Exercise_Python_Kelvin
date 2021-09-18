
class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def Insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.Insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.Insert(value)
        
    def PrintTree(self):
        if self != None:
            if self.left is not None:
                self.left.PrintTree()
            print(self.value, end=' ')
            if self.right is not None:
                self.right.PrintTree()
        return self
    
    def Contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.Contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.Contains(value)
        
    def Remove(self, value, parent = None):
    
    # Traverse through the list and find the actual value
        if value < self.value:
            if self.left is not None:
                self.left.Remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.Remove(value, self)
    # Actual deletion underneath, execute a few things when we found the value:
    # Scenario 1 when there is 2 nodes.
    # Deleting it require us to find the min value on the right and replacing it

    # Scenario 1A Deleting when its root with two child
        else:  
            if self.left is not None and self.right is not None: 
                self.value = self.right.MinValue()
                self.right.Remove(self.value, self)
    # Scenario 1B Deleting root with one node
            elif parent is None:
                if self.left is not None:      # 1B Deleting root one node, transfer
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:   # 1B Deleting root one node, transfer
                    self.value = self.right.value 
                    self.right = self.right.right 
                    self.left = self.right.left
                else:                          # Do nothing if its one node
                    pass 
    # Scenario two if deleting in the middle of the chain
            elif parent.left == self: # Comparing whether the parent.left object is equal to current object
                if self.left is not None:     # 2A Delete node in the middle to left, when one node to the left
                    parent.left = self.left
                else:                         # 2B Delete node in the middle to left, when one node to the right
                    parent.left = self.right
            elif parent.right == self:
                if self.right is not None:    # 2C Delete node in the middle to right, when one node to right
                    parent.right = self.right
                else:
                    parent.right = self.left   # 2D Delete node in the middle to right, when one node to left
        return self

    def FindClosestValue(self, tree, target):
        closest = tree.value
        currentNode = tree
        while currentNode is not None:
            if abs(target - currentNode.value) < abs(target - closest):
                closest = currentNode.value
            elif target < currentNode.value:
                currentNode = currentNode.left 
            elif target > currentNode.value:
                currentNode = currentNode.right
            else:
                break
        return closest 

    def MinValue(self):
        if self.left:
            return self.left.MinValue()
        else:
            return self.value

    # InOrder Traversal is a method to traverse based on the condition (Left, Root, Right)
    # On a Binary Tree, prints from smallest to largest
    # Left first, then right.
    # Pseudo code - 
    # Recursively travel left
    # Visit Root
    # Recursively travel right

    def InOrderTraversal(self):
        if self.left is not None:
            self.left.InOrderTraversal()
        print(self.value, end=' ')
        if self.right is not None:
            self.right.InOrderTraversal()

        
    # PreOrder Traversal - a method to travel tree based on the condition (Root, Left, Right)
    # Pesudo code
    # Visit Root
    # Recursively traverse left
    # Recursively traverse right

    def PreOrderTraversal(self):
        print(self.value, end = ' ')
        if self.left is not None:
            self.left.PreOrderTraversal()
        if self.right is not None:
            self.right.PreOrderTraversal()


    # PostOrder Traversal - a method to travel tree based on condition (Left, Right, Root)
    # Pseudo code:
    # Recursively travel left
    # Recursively travel right
    # Visit Root

    def PostOrderTraversal(self):
        if self.left is not None:
            self.left.PostOrderTraversal()
        if self.right is not None:
            self.right.PostOrderTraversal()
        print(self.value, end = ' ')


    def Depth(self, depth=0):
        if self is None:
            return 0
        return 

# root = Tree(10)
# root.Insert(5)
# root.Insert(15)
# root.Insert(7)
# root.Insert(7)
# root.Insert(8)

# root.PrintTree()
# # print(root.value, root.left.value, root.right.value)
# print(root.Contains(5))

# root.Remove(10)
# root.PrintTree()

root = Tree(27)
root.Insert(14)
root.Insert(35)
root.Insert(10)
root.Insert(19)
root.Insert(31)
root.Insert(42)

print('\nIn Order Traversal:')
root.InOrderTraversal()
print('\nPre Order Traversal:')
root.PreOrderTraversal()
print('\nPost Order Traversal:')
root.PostOrderTraversal()