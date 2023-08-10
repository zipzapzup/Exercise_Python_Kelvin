# Linked list
# 
# linked list need to maintain the head
#
# O(1) Operation Insert
# O(1) Operation Top Lookup
# Implementation of single linkedlist
# Node object is nested for convenience
class LinkedList:
    head = None
    length = 0

    class Node:
        __slots__ = "element", "next"

        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self, node):
        newNode = LinkedList.Node(node)
        self.head = newNode
        self.length += 1
        
    def push(self, e):
        newNode = LinkedList.Node(e)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise Exception("Error length is 0")
        currentHead = self.head
        self.head = currentHead.next
        return currentHead

    def __len__(self):
        return self.length
    
    def top(self):
        return self.head
    
    def listprint(self):
        current = self.head
        while current is not None:
            print(current.element, end= " ")
            current = current.next

    



a1 = LinkedList(5)
a1.push(10)
a1.push(20)
a1.push(30)
a1.push(40)
print(a1.length, a1.head.element, a1.head.next.element)
print(a1)
print("Singly Linked List Operation:")
a1.listprint()
print()


# Double Linked List
# O(1) Operation in insert
# O(1) Operation Delete
# O(1) Operation in view top
class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, element):
        newNode = Node2(element)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode            

    def pop(self):
        newHead = self.head.next
        temp = self.head
        newHead.prev = None
        self.head = newHead
        return temp

    def listnode(self):
        currentIteration = self.head
        while currentIteration is not None:
            print(currentIteration.data, end=" ")
            currentIteration = currentIteration.next

print("Double Linked List Operation:")
d1 = DoubleLinkedList()
d1.insert(5)
d1.insert(7)
d1.insert(8)
d1.insert(99)
d1.insert(99)
d1.pop()
d1.listnode()
