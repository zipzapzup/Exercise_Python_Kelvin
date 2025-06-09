# C:\Python36\
import math

print("{}testing a function".format('kelvin'))


# Create a function to calculate the area of a sphere.
def AreaSphere(r):
    v =  4.0 / 3.0 * math.pi * r **3
    return v

# Create a function to calculate the area of a circle
def AreaCircle(r):
    A = math.pi * r ** 2
    return A

# Create function to calculate the area of a square
def AreaSquare(w, l):
    # w stands for width and l stands for length
    A = w * l
    return A

# Create a function to calculate the area of a Triangle
def AreaTriangle(b, h):
    # b stands for base and h stands for height
    A = b * h / 2.0
    return A

AreaSphere(10)
AreaCircle(10)
AreaSquare(10,2)
AreaTriangle(5,7)

# Creating a function to call which number is higher
def highernumber(a, b):
    print('Hello there, this function will differentiate between a and b')
    if a > b:
        print ('{} is higher'.fomat(a))
    elif a < b:
        print ("{} is higher".format(b))
    else:
        print("{} is equal!".format(a))


highernumber(3,10)
highernumber(3,4)

def say(message, number=1):
    print(message * number)

say('HI world \n')
