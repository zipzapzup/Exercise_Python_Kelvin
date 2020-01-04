# Exercises 1
def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False

print("EX1: "+ str(is_multiple(10,2)))

# Exercises 2
def is_even(k):
    result = divmod(k,2)
    if result[1] == 0:
        return True
    else:
        return False

print("EX2: " + str(is_even(4)))

# Created a check for iseven using a loop and range. Where the range becomes the pivor based on the index. Range + 1 because range always fall short by 1.
def is_even2(k):
    isEven = True
    for i in range(1,(k+1)):
        if isEven == True:
            isEven = False
        elif isEven == False:
            isEven = True
    return isEven



# Exercises 3
def minmax(data):
    min = data[0] 
    max = data[0]
    # define minimum first
    for i in range(len(data)):  
        if data[i] < min:
            min = data[i]
        else:
            continue
    for j in range(len(data)):
        if data[j] > max:
            max = data[j]
        else:
            continue
    return min, max

print("EX3: " + str(minmax([3,2,7,4])))

# Exercises 4
def sumsquare(n):
    if n < 0:
        raise ValueError("Invalid number, n must be postive")
