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
            if len(currentTree.children) > 0:
                allnode = allnode + currentTree.children
            print(currentTree.data)
                

    def countNodes(self):
        nodes = [self]
        sum = 0
        while len(nodes) > 0:
            current = nodes.pop()
            sum += 1
            nodes = nodes + current.children
        return sum

    def preorderTraversal(self, root):
        print(self.data)



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

    def height(node):
        if self.
    # preorder traversal
    # root > left > right
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

    # post order traversal
    # left > right > root
    # visits
    # O(n) Complexity
    def postorderTraversal(self):
        visit = []
        if self:
            visit = self.postorderTraversal(self.right)
            visit = self.postorderTraversal(self.left)
            visit.append(self.data)
        return visit
    
    # in order traversal
    # left > root > right
    # O(n) Complexity
    # print in ascending order
    def inorderTraversal(self):
        visit = []
        if self:
            visit = visit + self.inorderTraversal(self.left)
            visit.append(self.data)
            visit = visit + self.inorderTraversal(self.right)
        return visit

    def preOrderTraversal(root):
        if root:
            print("PreOrder Traversal: ", root.data)
            preOrderTraversal(root.left)
            preOrderTraversal(root.right)

    def PostOrderTraversal(root):
        if root:
            postOrderTraversal(root.left)
            postOrderTraversal(root.right)
            print("PostOrder Traversal: ", root.data)

    def InOrderTraversal(root):
        if root:
            InOrderTraversal(root.left)
            print("InOrder Traversal: ", root.data)
            InOrderTraversal(root.right)

    def preOrderTraversalv2(root):
        if root is None:
            return
        print("Preorder Traversal:", root.data)
        preOrderTraversalv2(self.left)
        preOrderTraversalv2(self.right)
    
    def postOrderTraversalv2(root):
        if root is None:
            return
        postOrderTraversalv2(self.left)
        postOrderTraversalv2(self.right)
        print("Postorder Traversal :", root.data)
    
    def inordertraversalv2(root) -> None:
        if root is None:
            return
        inordertraversalv2(root.left)
        print("InOrder Traversal :", root.data)
        inordertraversalv2(root.right)
