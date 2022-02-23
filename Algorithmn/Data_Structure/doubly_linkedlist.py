# Doubly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class LinkedList2:
    def __init__(self, data):
        newNode = Node(data)
        self.head = newNode
        self.capacity = 0
        self.tail = newNode

    # Insert at head
    # O(1) Time, O(1) Space
    def insert(self, data):
        newNode = Node(data)
        self.head.left = newNode
        newNode.right = self.head
        self.head = newNode

    # O(N) Time O(1) Space
    def insert_position(self, position, data):
        newNode = Node(data)
        count = 0
        currentNode = self.head
        while currentNode:
            if count == position:
                if currentNode.left is None:
                    currentNode.left = newNode
                    newNode.right = currentNode
                    self.head = newNode
                else:
                    Prev = currentNode.left
                    Prev.right = newNode
                    newNode.right = currentNode
                    currentNode.left = newNode
                break
            currentNode = currentNode.right
            count += 1

    # O(1) Time and Space
    def print_head(self):
        print(self.head.value, self.head.right, self.head.left)

    # O(1) Time and Space
    def remove_head(self):
        currentNode = self.head
        self.head = self.head.right
        del currentNode
        self.head.left = None

    # Print all list from head
    # O(n) Time O(1) Space
    def print(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=' ')
            currentNode = currentNode.right
        
a = Node(5)
DoubleLinked = LinkedList2(10)
DoubleLinked.insert(8)
DoubleLinked.insert(100)
DoubleLinked.insert(1)
DoubleLinked.insert(5)
DoubleLinked.print()
print('\nfirst result')
DoubleLinked.insert_position(2,7)
DoubleLinked.insert_position(0,0)
DoubleLinked.print()
print('\nsecond result')
DoubleLinked.insert_position(0,3)
DoubleLinked.print()
DoubleLinked.remove_head()
DoubleLinked.remove_head()
print('\nthird result')
DoubleLinked.print()