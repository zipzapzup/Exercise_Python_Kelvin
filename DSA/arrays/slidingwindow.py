
from sys import maxsize
array = [1,3,10,5,20,10,15]

# sliding window approach
# to solve the maxSum 
# O(n) time operation
def maxSum(array, size):
    maxSum = 0
    for i in range(len(array) - size + 1):
        total = sum(array[i: i + size])
        if total > maxSum:
            maxSum = total
    return maxSum
            

print(maxSum(array, 2))



print(-maxsize)