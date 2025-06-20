# Tree
from collections import deque

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

# DFS (Depth First Search)
# inorder: left, root, right
# postorder: left, right, root
# preorder: root, left, right

class BinaryTree:
    def __init__(self, data, left=None, right =None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = data
                else:
                    self.right.insert(data)
        else:
            self.data = data


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
    # O(h) height of tree is the Space Complexity
    #       - Complete Binary Tree (Log N)
    #       - Skewed Tree (h)
    def inorderTraversal(self):
        visit = []
        if self:
            visit = visit + self.inorderTraversal(self.left)
            visit.append(self.data)
            visit = visit + self.inorderTraversal(self.right)
        return visit

    def preOrderTraversal(self, root):
        if root:
            print("PreOrder Traversal: ", root.data)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    def PostOrderTraversal(self, root):
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print("PostOrder Traversal: ", root.data)

    def InOrderTraversal(self, root):
        if root:
            self.InOrderTraversal(root.left)
            print("InOrder Traversal: ", root.data)
            self.InOrderTraversal(root.right)

    def preOrderTraversalv2(self, root):
        if root is None:
            return
        print("Preorder Traversal:", root.data)
        self.preOrderTraversalv2(self.left)
        self.preOrderTraversalv2(self.right)
    
    def postOrderTraversalv2(self,root):
        if root is None:
            return
        self.postOrderTraversalv2(self.left)
        self.postOrderTraversalv2(self.right)
        print("Postorder Traversal :", root.data)
    
    def inordertraversalv2(self, root) -> None:
        if root is None:
            return
        self.inordertraversalv2(root.left)
        print("InOrder Traversal :", root.data)
        self.inordertraversalv2(root.right)

    # Breath First Search
    # BFS
    # O(n) Time Complexity *armortised
    # O(n) Space complexity
    def BFS(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            print(queue[0], end=" ")
            current = queue.pop(0)
            if current.left is not None:
                queue.append(current.left)
            
            if current.right is not None:
                queue.append(current.right)
        

    # Optimised BFS
    # Breath First Search
    # O(n) Time Complexity
    # O(n) space complexity    

    def BFSOptimised(self, root):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            print(queue[0].data, end= " ")
            current = queue.popleft()
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    # height of tree
    # can be found by finding the maximum depth
    # in the case where root is None, its 0
    # otherwise if root exist, then the height is at least one
    # now, you want to return the max between these two
    def treeHeight(self, root):
        if root is None:
            return 0
        lheight = self.treeHeight(root.left)
        rheight = self.treeHeight(root.right)

        return max(lheight, rheight) + 1