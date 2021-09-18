print("Hello World")

# Solving a Factorial problem
# 5! = 5x4x3x2x1

def Recursive(n):
    # In recursive function, you need the condition of stopping value
    #
    if n == 1:
        return n
    else:
        return n * Recursive(n-1)
    

def IterativeA(n):
    # Solve Factorial problem iteratively
    total = 1
    for i in range(n,1,-1):
        total *= i
    return total

def IterativeB(n):
    total = 1
    while n >= 1:
        total *= n
        n = n-1
    return total