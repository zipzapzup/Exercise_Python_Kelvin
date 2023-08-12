import heapq

# HeapSort
# is a Complete BinaryTree 
# Operations in Heap
# HeapSort - N Log N
# Insert Operation - Log(N)
# Remove Operation - Log(N)
# Largest Element - O(1)

# Space Complexity O(1) Auxiliary Space (Extra Space)
# this is so because it can sort in place via heapify
# see version 2

# 2 Methods exist
# Min Heap
# Max Heap

array = [19,3,10,4,19,9,1,20,3,8,9,39]
def minHeapSort(n: list):
    minHeap = []
    # N Time Complexity
    for i in n:
        heapq.heappush(minHeap, i) # Log N Complexity
    while minHeap:
        print(heapq.heappop(minHeap), end=" ")


def maxHeapSort(n: list):
    maxHeap = []
    for i in n:
        heapq.heappush(maxHeap, -1 * i)
    while maxHeap:
        print(-1 * heapq.heappop(maxHeap), end = " ")


array2 = [19,3,10,4,19,9,1,20,3,8,9,39]
array3 = [19,3,10,4,19,9,1,20,3,8,9,39]

# Time Complexity N Log(N)
# Space O(1) Auxiliary Space / modify in place
def minHeapSort2(n: list):
    heapq.heapify(n)
    while n: # N Time Complexity
        print(heapq.heappop(n), end= " ") # LogN Time Complexity

# Time Compelxity N Log(N)
# Space O(1) Auxiliary Space / Modify in Place
def maxHeapSort2(n: list):
    heapq._heapify_max(n)
    while n:
        print(heapq._heappop_max(n), end=" ")


print("\nStarting MinHeap")
minHeapSort(array)

print("\nStarting MaxHeap")
maxHeapSort(array)

print("\nStarting MinHeap2")
minHeapSort2(array2)

print("\nStarting MaxHeap2")
maxHeapSort2(array3)