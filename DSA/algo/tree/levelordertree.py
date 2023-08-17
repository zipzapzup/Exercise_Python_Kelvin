from collections import deque

class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, data):
        newTree = BinaryTree(data)
        if data < self.val:
            if self.left:
                self.left.insert(data)
            else:
                self.left = newTree
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = newTree


    def preorderTraverse(self, root):
        # root, left, right
        visit = []
        if root is None:
            return visit
        
        visit.append(root.val)
        visit += self.preorderTraverse(root.left)
        visit += self.preorderTraverse(root.right)
        return visit
    
    def inorderTraverse(self, root):
        # left, root, right
        visit = []
        if root is None:
            return visit
        
        visit = visit + self.inorderTraverse(root.left)
        visit.append(root.val)
        visit = visit + self.inorderTraverse(root.right)
        return visit

    def postorderTraverse(self, root):
        # left, right, root
        visit =[]

        if root is None:
            return visit
        visit = visit + self.postorderTraverse(root.left)
        visit += self.postorderTraverse(root.right)
        visit.append(root.val)
        return visit
    
    def levelorderTraverse(self, root):
        # level by level
        # root, left, right
        # implement using queue - popleftl
        if root is None:
            return
        stack = deque()
        queue = deque()
        queue.append(root)
        while queue:
            currentNode = queue.popleft()
            # stack is what we are returning
            stack.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return stack
        
    def printlevelorder(self, root):
        # level order print
        if root is None:
            return
        queue = deque()
        queue.append(root)
        while queue:
            currentNode = queue.popleft()
            print(currentNode.val, end=" ")
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
    def sumNodes(self, root):
        count = 0
        if root is None:
            return count
        count += root.val
        if root.left:
            count += self.sumNodes(root.left)
        if root.right:
            count += self.sumNodes(root.right)
        return count



# construct binary tree

root = BinaryTree(10)
root.insert(5)
root.insert(50)
root.insert(55)
root.insert(5)
root.insert(40)
root.insert(35)
root.insert(1)
root.insert(2)


print(root.preorderTraverse(root), " preorder")
print(root.inorderTraverse(root), " inorder")
print(root.postorderTraverse(root), " postorder")
print(root.levelorderTraverse(root), "levelorder")


root.printlevelorder(root)

print("\nSum of All Nodes", root.sumNodes(root))