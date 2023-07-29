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