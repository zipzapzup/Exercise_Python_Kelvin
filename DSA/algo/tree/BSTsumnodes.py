# Sum Nodes in Between Trees


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, newval):
        newNode = BinaryTree(newval)
        if newval <= self.val:
            if self.left:
                self.left.insert(newval)
            else:
                self.left = newNode
        if newval > self.val:
            if self.right:
                self.right.insert(newval)
            else:
                self.right = newNode


# Breadth First Search (BFS), level order
# Recursive approach
    def bfsRecursive(self, root, low, high):
        answer = 0
        def bfs(node):
            nonlocal answer
            if node:
                if node.val >= low and node.val <= high:
                    answer += node.val
                if node.left:
                    bfs(node.left)
                if node.right:
                    bfs(node.right)
        bfs(root)
        return answer
    
    # bfs Breadth First Search (BFS), level order traversal
    # Iterative approach
    def bfsIterative(self, root, low, high):
        sum = 0
        if root is None:
            return sum
        
        stack = [root]
        while stack:
            currentNode = stack.pop()
            if currentNode:
                if currentNode.val >= low and currentNode.val <= high:
                    sum += currentNode.val
                stack.append(currentNode.left)
                stack.append(currentNode.right)
        return sum


newtree = BinaryTree(10)
newtree.insert(5)
newtree.insert(7)
newtree.insert(9)
newtree.insert(15)

print(newtree.bfsRecursive( newtree, 9, 10))

print(newtree.bfsIterative(newtree, 9,10))