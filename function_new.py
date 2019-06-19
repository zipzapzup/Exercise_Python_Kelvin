# C:\Python36\
impor math

print("{}testing a function".format('kelvin'))


# Create a function to calculate the area of a sphere.
def AreaSphere(r):
    v =  4.0 / 3.0 * math.pi * r **3
    return v

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
