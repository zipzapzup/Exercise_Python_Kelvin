import time, sys
## Arrays (lists)
# O(1) Get and Update
# O(n) Append or Insertion
# O(n-i) Delete

arr = [1,2,3]
print(arr)

# Stack implementation
arr.append(5)
arr.append(10)
print(arr)

arr.pop()
print(arr)

# insert at specific index is O(N) operation
arr.insert(1,6)
print(arr)

# array indexing is O(1) constant time
# set operation O(1)
arr[1] = 2

# get operation O(1)
arr[0]

arr2 = [1,2,3,4,5]
# 1,2,3,4,5
# entire array
arr[0:5]

# entire array -1
arr[0:4]

# 1,2
arr[0:2]

# gets it on reverse
# 5,4,3,2,1
arr[::-1]

# unpacking array
a1, b1, c1 = [1,2,3]

# Loop through array
# using index
nums = ["a","b","c", "d", "e"]
for i in range(len(nums)):
    print("using index: ",i)

# using the value
for i in nums:
    print(i)

# using index and value via enumerate
for index, value in enumerate(nums):
    print(index, value)


# reverse method on array
nums.reverse()
print(nums)

# sorting array
# sort in ascending order by default
# BigO( NlogN)
arr = [5,3,1,2,3,5,5]
arr.sort()
print(arr)

# reverse the sort in descending order
arr.sort(reverse=True)

# sort can do string too
arr10 = [ "Bob", "jill", "jane", "doe"]
arr10.sort()
print(arr10)

# custom
# sort via key in ascending order
arr10.sort(key= lambda x: len(x))

# sort via keys in descending order
arr10.sort(key= lambda x: len(x), reverse=True)


# Array or Lists
# List comprehension
# [1,2,3,4,5,6,7,8,9,10]
arr11 = [i+1 for i in range(10)]
print(arr11)


# 2D Arrays
# build 2D Arrays via list comprehensions
arr12 = [ [0]* 5 for i in range(5) ] 

# this prints the array
for i in arr12:
    print(i)


# given a list of arrays in integers  
# sort the value so that the even is on the left
# where A is a list of integers
# O(n) Time Complexity
# O(1) Space
def sortEvenOdd(A):
    ptrA, ptrB = 0, len(A) - 1
    while ptrA < ptrB:
        if A[ptrA] % 2 == 0:
            ptrA += 1
        else:
            A[ptrA], A[ptrB] = A[ptrB], A[ptrA]
            ptrB -= 1


A = [9,1,3,20,10,49,10,8,10,7,9]
sortEvenOdd(A)
print(A)

c1 = [1,2,3,4,5]

# shallow copy share pointer and objects
c2 = c1

# deep copy creates independent object
c3 = c1.copy()

# list comprehension (arrays)

a1 = [ x**2 for x in range(5) if x % 2==0]


# Σ : x1, x2, x3, x4, x5
# Sigma on the sum of all of list above
# where x = [x1, x2, x3, x4, x5]
# can be computed via 
# the following function representation
def sigmaAdd(x):
    sum = 0
    for i in x:
        sum += i
    return sum



# find max number in an element
# O(n) time
def findMax(x):
    max = 0
    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
    return max

# find the average of the array
# return to 2 floating number
# 2 decimal places
def average(array):
    sum = 0
    length = len(array)
    for i in array:
        sum += i
    return round(sum / length, 2)


# Two Types of Arrays in Python
# Dynamic Arrays : Lists
# Fixed size Arrays, compact arrays: Strings, Tuples
#
# List in python is a dynamic array
# that holds a containers which provides a 
# referential type of data structure

data = []
for i in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in Bytes: {1:4d}'.format(a,b))

# Under the hood
# when Dynamic Array is expanded beyond the capacity
# O(n) Time Complexity operation
# 
# # Length:   0; size in bytes:   56
# Length:   1; size in bytes:   88
# Length:   2; size in bytes:   88
# Length:   3; size in bytes:   88
# Length:   4; size in bytes:   88
# Length:   5; size in bytes:  120
# Length:   6; size in bytes:  120
# Length:   7; size in bytes:  120
# Length:   8; size in bytes:  120
# Length:   9; size in bytes:  184
# Length:  10; size in bytes:  184
# Length:  11; size in bytes:  184
# Length:  12; size in bytes:  184
# Length:  13; size in bytes:  184
# Length:  14; size in bytes:  184
# Length:  15; size in bytes:  184
# Length:  16; size in bytes:  184
# Length:  17; size in bytes:  256

# high score array
# insert O(n) Time Complexity
# insert high score if the score is bigger than the previous
highscore = [0] * 10
def insertScore(data, score):
    n = len(data) - 1
    
    while n > 0 and data[n-1] < score:
        data[n] = data[n-1]
        n -= 1
    data[n] = score


insertScore(highscore, 10)




