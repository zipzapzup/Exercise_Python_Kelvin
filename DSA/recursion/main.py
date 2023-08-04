# recursion

# factorial
# return a factorial of n!
# using recursive
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)