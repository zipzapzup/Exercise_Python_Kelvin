# Exercising Algorithmn


def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False

# R11 - Big(O): O(1) ST
print('Exercise R1.1:', is_multiple(10,10))


def is_even(k):
    if k % 2 ==0:
        return True
    else:
        return False
# R12 - Big(O): O(1) ST

print('Exercise R1.2:', is_even(20))

def minmax(data):
    container = data
    min = container[0]
    max = container[0]
    for i in range(len(container)):
        if container[i] > max:
            max = container[i]
        if container[i] < min:
            min = container[i]
        else:
            pass
    return "Min is:", min,"Max is:", max
# Big(O): O(n) ST
print('Exercise R1.3:', minmax([100,2,3,4,5,6,9]))

def sumsquares(n):
    return sum([i*i for i in range(n)])

# Big(O): O(n) ST 
print('Exercise R1.4:', sumsquares(5))


def sumsquaresodd(n):
    return sum([i*i for i in range(1,n,2)])

#Big(O):  O(0.5n) ST, however it still translates to O(n) ST
print('Exercise R1.6:', sumsquaresodd(5))

# R-1.8 Equivalent index such that s[j] reference the same element would be:
print('Exercise R1.8: Answer is j = n + k')

print("Exercise R1.9: Answer is range(50,90,10)",list(range(50,90,10)))
#Big(O) of O(1) ST. Range is a constant operations even when the input grows.

print('Exercise R1.10: Answer is range(8,-9,-2)', list(range(8,-9,-2)))
#Big(O) is O(1) ST. Range is a constant operations as input grows.

print('Exercise R1.11:', [2**n for n in range(9)])


print("Exercise C1.13:", """
N -> is a list of integers

Create a function that take N as an integers
1. Create a variable for storing
2. For loop through N in reverse order
3.     Each time the loop goes through N, appends the value from the back
4. Save the variable and return the list
""")

def distinctodd(data):
    result = []
    Odd = False
    for i in range(len(data) -1 ):
        for k in range(i + 1,len(data)):
            if (data[i] * data[k]) % 2 == 1:
                return True
            else:
                continue
    return Odd
# Big(O) = O(n^2) ST due to the fact we are looping through the value twice in the loop.
print("Exercise C1.14:", distinctodd([2,7,4,3,2,2,4,8,20]))
