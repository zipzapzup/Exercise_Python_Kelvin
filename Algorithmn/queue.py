

from collections import deque 
# queue python implementation - optimised

queue = deque() 

queue.append(1)
queue.append(2)
queue.append(100)
queue.append(7)
queue.append(2)

print(queue)

x = queue.popleft()
print(x)
print(queue)