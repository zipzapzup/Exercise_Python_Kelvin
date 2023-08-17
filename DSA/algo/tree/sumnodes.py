from collections import deque

class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, val):
        newTree = BinaryTree(val)
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = newTree
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = newTree
    
    # O(2n) -> O(n) Time Operation - tree
    # O(n) Space Complexity
    def sumNodesRecursive(self, root) -> int:
        count = 0
        if root is None:
            return 0 #O(1)
        return root.val + self.sumNodesRecursive(root.left) + self.sumNodesRecursive(root.right)

    def sumNodes(self, root) -> int:
        # preorder traversal
        count = 0

        currentNode = root
        if currentNode is None:
            return count
        
        count += currentNode.val
        if currentNode.left:
            count += currentNode.sumNodes(currentNode.left)
        if currentNode.right:
            count += currentNode.sumNodes(currentNode.right)
        return count
    
    def inordersumNodes(self, root):
        # in order
        count = 0
        currentNode = root
        if currentNode is None:
            return count
        
        if currentNode.left:
            count += currentNode.inordersumNodes(currentNode.left)
        count += currentNode.val
        if currentNode.right:
            count += currentNode.inordersumNodes(currentNode.right)
        return count
    
    def postordersumNodes(self, root):
        count = 0 
        currentNode = root
        if currentNode is None:
            return count
        
        if currentNode.left:
            count += currentNode.postordersumNodes(currentNode.left)
        if currentNode.right:
            count += currentNode.postordersumNodes(currentNode.right)
        count += currentNode.val
        return count
    
    # breath first search
    def BFSsumNodes(self, root):
        count = 0
        queue = deque()
        if root is None:
            return count
        queue.append(root)

        while queue:
            current = queue.popleft()
            count += current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return count



root = BinaryTree(10)
root.insert(5)
root.insert(9)
root.insert(8)
root.insert(20)
root.insert(25)
root.insert(30)
root.insert(1)
root.insert(2)
root.insert(100)


print(root.sumNodes(root), "preorder sumnodes")
print(root.inordersumNodes(root), "inorder sumnodes")
print(root.postordersumNodes(root), "postorder sumnodes")
print(root.BFSsumNodes(root), "BFS level order")
print(root.sumNodesRecursive(root), "Recursive")

root2 = BinaryTree(10)
root2.insert(1)
root2.insert(2)
root2.insert(3)

print(root2.sumNodes(root2), "preorder sumnodes")
print(root2.inordersumNodes(root2), "inorder sumnodes")
print(root2.postordersumNodes(root2), "postorder sumnodes")
print(root2.BFSsumNodes(root2), "BFS level order")
print(root2.sumNodesRecursive(root2), "Recursive")