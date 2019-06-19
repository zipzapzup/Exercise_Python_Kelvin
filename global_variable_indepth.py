# C:\Python36\
print ("Kelvin Script, exploring global variable")
x = 50


def func():
    global x
    print ("x is:{}".format(x))
    x = 2
    print ("Changed global x to:{}".format(x))


func()
print("After the changes, x becomes {}".format(x))



# Test number
