hashmap = {}

# initialise
hashmap = {"bonjor": 10, "will" : 30}

# hashmap
# O(1) operation in set - average. Worst armortized: O(N)
# O(1) operation in get - average. Worst armortized: O(N)
# O(1) operation in check - average. Worst armortized: O(N)
# O(1) operation in del - average. Worst armortized: O(N)


# set
hashmap["john"]  = 10
hashmap["bob"] = 20


# get
hashmap["john"]

# check
"john" in hashmap

# del
del hashmap["john"]

# loop O(n) of course
# loop through key
for i in hashmap:
    print(i, hashmap[i])


# loop through values
for i in hashmap.values():
    print(i)

# loop through items (unpacking)
for key, item in hashmap.items():
    print(key, item)