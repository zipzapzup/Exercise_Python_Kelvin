# C:/Python36

print("Kelvin's fifth script - docstring statement")

def print_max(x, y):
    ''' This is basically the help line and the doc string:
    - print the maximum of two numbers.
    - the two values are integers.'''

    # Convert the x and y value to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is the maximum')
    else:
        print(y, 'is the maximum')

print_max(3,5)
print(print_max.__doc__)
