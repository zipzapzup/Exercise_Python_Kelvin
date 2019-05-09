# C:\Python36
print ("This is Kelvin2 Script - testing argument values")

def say(message, times=1):
    print(message * times)
say("Hello\n", 2)
## Argument variable can be defined inside the function after say()
## Argument is also useful, when assigned a specific number of time
## When you assgined a value in the argument, it specifies the default value, however it is overriden if there is another function in it

def func(a, b=5, c=10):
    print('a is{}'.format(a), ' and b is{}'.format(b), 'and c is{}'.format(c))

func(3,7)
func(25, c=24)
func(c=2, a=100)
