# heap
import heapq

# under the hood are arrays
# min heap is a binary tree data structure
# where the root node is the minimum value
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 4)

# Min is at index 0
minHeap[0]


# smallest to largest - minheap
# while loop will print them 
# 3,4,5
while len(minHeap):
    print(heapq.heappop(minHeap))






# Max heaps
# max heap is a binary tree data structure
# where root node is the max value

# implementation via array and heapq
# implement max heap via negative value
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -5)
heapq.heappush(maxHeap, -4)

# Max is at index 0
print(-1 * maxHeap[0])

# print the maxheap value
# in order of biggest to smallest
# 5,4,3
# negate the -1
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))





# build initial values

arr = [2,1,4,7,1,2]

# initialisation
# linear time O(n)
heapq.heapify(arr)

# minheap to the arr
# prints in ascending order
while arr:
    print(heapq.heappop(arr))

