# C:\Python36\

print("{}testing a function".format('kelvin'))



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
