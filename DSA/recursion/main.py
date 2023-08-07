# recursion
# 1. Singular Recursion
# 2. Binary Recursion
# 3. Many Recursion

# factorial
# return a factorial of n!
# using recursive
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


# Fibonaci number
# Complexity is O(2^n)
# More functions get executed the larget the value of n
# c0 is n = 1
# c1 is n = 0
# c2 is n = 3 (fib(1) + fib(0) + fib(0))
# c3 is n = 5 (fib(1) + fib(0)+ fib(1))
# c4 is n = 
# Example of Binary Recursion
def getFibonaci(n: int)-> int:
    if n == 1 :
        return 1
    elif n == 0:
        return 1
    else:
        return getFibonaci(n-1) + getFibonaci(n-2)
    

# LinearSum
# via recursion
# O(n) Space and Time Complexity
# Singular Recursion
def linearSum(element: list, n: int):
    if n == 0:
        return 0
    else:
        return linearSum(element, n-1) + element[n-1]
    


# Compute Power of
# recursive
# O(n) ST - linear recursion
def powerOf(base, power):
    if power == 0:
        return 1
    else:
        return powerOf(base, power -1) * base