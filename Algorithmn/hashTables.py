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
print(Dict1)

a = "".join(Dict1.values())
print(a)