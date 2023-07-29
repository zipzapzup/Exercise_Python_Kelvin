# hashset - mutable
# contains no duplicate and unordered element
# {"apple", "orange", "watermelon"}
# hset = set([iterables])
hashset = set()

# O(1) average case - add
hashset.add(10)
hashset.add(11)
hashset.add(13)


# O(1) average case - remove
hashset.remove(20)

# O(1) average case - check
# hash set b
10 in hashset
10 not in hashset

print(len(hashset))



# frozen set - immutable
# O(1) operation for get in average
hashfrozen = frozenset()


# set comprehension
mySet = {i for i in range(5)}

# Looping through set
# of course O(n)
for i in hashset:
    print(i)


# A = {1,2,3}
# B = {3,4,5}

# Union operator (O(n times m)) 
# union set(A) | set(B)
# returns all a and b
# {1,2,3,4,5}


# Itersection operator 
# union set(A) & set(B)
# returns whats common between
# {3}


# difference operator
# union set(A) - set(B)
# return the difference
# {1,2}