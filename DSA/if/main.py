print("Hello")

x = 10
if x != 10:
    print("X is not 10")

a = True and True
print("A is", a)



def absoluteValue(n):
    if n < 0:
        return -n
    return n

if __name__ == "__main__":
    print("Hello World, Starting up")
    
    print(absoluteValue(-10))