# BST - Binary Search Tree
# is a tree where it can hold a key value pair
# a Binary Search Tree is as follows
# followed by a class of a Node
# and a Binary Search Tree class


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)