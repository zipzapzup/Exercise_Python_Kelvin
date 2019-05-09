# C:/Python36
# Module lesson2, using from..import statements, allow you to directly import statement to your programself.
# This mean that you don't have to type sys.argv for it and can type it directly as sys.

from math import sqrt
print("Square root of 16 is", sqrt(16))
# Note, if we didnt use from, we need to write math.sqrt(16)



# Using __main__ to check whether the module is run by itselves or imported.
# If you run python module2.py, you will notice that this module is run by itselvesself.
# However if you are using python interactive mode, it will mention that it is imported from another module

if __name__ == '__main__':
    print("This program is being run by itself")
else:
    print("I am imported from another module")


# Note, if we didnt use from, we need to write math.sqrt(16)
