newDict = {
    1 : "John",
    9 : "SMoke",
    19: "Poke",
    98: "John1",
    -10: "Poikl"

}

print(newDict)

print(newDict[9])

Dict1 = sorted(newDict.items())
print("Sorted: ", Dict1)

a = "".join(str(Dict1))
print("A is:", a)


items1 = dict({"key1" : 1, "key2": 2 , "key3" : 3})
print(items1)



# iterate items and values on hashtables

for key, value in items1.items():
    print("key: ",key, " value: ", value) 