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

