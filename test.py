#! C:\Python36
print("Hello there!")
print("We are going to be testing local and global variable")

x = 20


def sayHello():
    global x
    print("x is ", x)
    x = 90
    print('I changed x to a local variable of', x)


sayHello()
print("x is after:", x)
