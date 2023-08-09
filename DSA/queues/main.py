from collections import deque

queue = deque()

# dequeue is double ended queue
# represented as doubly linked list
# offers fast operations
# O(1) append right or left 
# O(1) pop right or left 
# O(n) accessing elements in the middle

# Append operation O(1) operation
queue.append(1)
queue.append(10)
print(queue)


# Append left operation O(1) operation
queue.appendleft(1)

# O(1) Operation
queue.popleft()
print(queue)

# O(1) Operation pop from right
queue.pop()
print (queue)

# make a shallow copy
queue.copy()

# clear the queue
queue.clear()

# remove first occurrence O(n)
queue.remove(1)



# Array implementation of queueu
# inefficient implementation
# dequeue is using a pop(0) 
# on all case it will be O(n)
# since it needs to shift the list
# O(1) append the queue - armortised to O(n)
# O(n) dequeue pop(0)
# 
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def queue(self, element):
        self.queue.append(element)

    def dequeue(self):
        return self.queue.pop(0)
    
    def __len__(self):
        return len(self.queue)
    

