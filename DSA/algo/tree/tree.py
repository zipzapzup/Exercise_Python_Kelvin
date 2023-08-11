# Tree

# normal tree implemenetation
# tree can have more than 1 child
# represented using a list
# inefficient tree structure
# O(n) operation for traverse
# O(1) operation for addChild *armortised
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.children = []

    def addChild(self, element):
        newTree = TreeNode(element)
        self.children.append(newTree)

    def removeChild(self, target):
        if target in self.children:
            self.children.remove(target)
        else:
            raise Exception("Child not found")
        
    def traverse(self):
        allnode = [self]
        while len(allnode) > 0:
            currentTree = allnode.pop()
            if currentTree.data is None:
                break
            else:
                print(currentTree.data)
            allnode = allnode + currentTree.children
        
    def countNodes(self):
        nodes = [self]
        sum = 0
        while len(nodes) > 0:
            current = nodes.pop()
            sum += 1
            nodes = nodes + current.children
        return sum


t1 = TreeNode(5)
t1.addChild(10)
t1.addChild(7)
t1.addChild(15)
t1.addChild(20)
t1.addChild(25)
t1.children[0].addChild(99)
t1.children[0].addChild(20)
t1.children[1].addChild(100)

t1.traverse()

print("Number of Nodes: ",t1.countNodes())

class BinaryTree:
    def __init__(self, data, left=None, right =None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = data
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = data
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # root node visited first
    # then left sub tree
    # and right sub tree
    # O(n) Time Complexity
    def preorderTraversal(self):
        visits = []
        if self:
            visits.append(self.data)
            visits = visits + self.preorderTraversal(self.left)
            visits = visits + self.preorderTraversal(self.right)
        return visits

    