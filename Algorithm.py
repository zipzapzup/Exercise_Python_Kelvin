import random

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
        a = i
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

# Exercises 4 and 5
def sumsquare(n):
    if n < 0:
        raise ValueError("Invalid number, n must be positive")
    totals = sum([i*i for i in range(n)])
    return totals

print("EX4:", sumsquare(5))

# Exercises 6 and 7
def squareodd(n):
    if n < 0:
        raise ValueError("Invalid number, n must be positive")
    totals = sum([i*i for i in range(n) if i % 2 == 1])
    return totals

print('Ex6, Ex7:',squareodd(5))

# Exercise 8
# Python allow negative integers as indices to a sequence. If string s has length n, and s[k] is used for index. What is the equivalent index such that s[j] references the same element.

# Inequalities problem
# s[k] = s[j]
# n = len(s)
# 
# -n <= k <0   and n >= j >= 0
#  n >= -k > 0 and n >= j >= 0
#  n >= -k > 0  =  n >= j >= 0
#  n + k >= 0 
# Answers is n + k
# Since n is len(s), to get the same position if k is a minus index
# string = "halo"
# s[-1] = o
# s[j] = 3
# n = 4
# Therefore s[j] = k + n, where k is a negative.

# Exercise 9
print("Ex9:", list(range(50,90,10)))

#Exercise 10
print("Ex10:", list(range(8,-9,-2)))

#Exercise 11
print("Ex11:", [pow(2,i) for i in range(9)])

#Exercise 12
def choice1(data):
    return data[random.randrange(len(data))]
print("Ex12:", choice1(['car','mobile','net']))

#Exercise 13
# Write a Pseudo code and algorithmn to reverse the list in order
# 1. This program will be a function that reverse the list from back to front.
# 2. It will take list as an input
# 3. And reverse it inside.

def reverselist(data):
    reverse = []
    for i in range(1, (len(data) + 1)):
        reverse.append(data[-i])
    return reverse
# Every list has a reverse method, where you can go with list.reverse()

print("Ex13:", reverselist(['car','bob','bird','wind']))

#Exercise 14
# Determine odd products from a sequence
def determineodd(data):
    assert type(data) == list, "Needs to be list"
    newlist = list(set(data)) # Remove duplicates
    # Start nested loop after here
    for i in range(len(newlist)):
        for k in range(len(newlist)):
            if newlist[i] != newlist[k]:
                product = newlist[i] * newlist[k]
                if product % 2 == 1:
                    return True
                else:
                    return False

print("Ex14:", determineodd([1,2,4,5]))

#Exercise 15
def determinedistinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

#Another way to solve 15
def distinct(data):
    for i in data:
        if data.count(i) > 1:
            return False
    return True


print("Ex15:", determinedistinct([1,3,5]))

#Exercise 16
# Integer is immutable and cannot be changed, however on the scale function, the assignment is made on the list element directly. List is mutable. KEY: data[j] =

#Exercise 17
# It will not work, since the assignment is made on val, which only exist on the local namespace and not a mutable instance. It is a temporary variable inside the function. KEY: val =

#Exercise 17
# def scale(data,factor):
#     for val in data:
#         val *= factor
# This will not work since you are making changes to val variable and val is only limited to the function scope, local namespace.

#Exercise 18
# Sequence: [0,2,6,12,20,30,42,56,72,90]
# Formula: n^2 + n
print("Ex18:",  [ (pow(i,2) + i) for i in range(10)])

#Exercise 19
# In here we utilise the use of chr and ord.
# chr() return the string representation for one character given the unicode point, for example chr(97) = 'a'
# ord() will return the unicode point for one character, example ord('a') = 97
# More information: https://www.rapidtables.com/code/text/unicode-characters.html

print("Ex19:", [chr(i) for i in range(97,123)])

#Exercise 20
# import random

def shuffle1(data):
    assert type(data) == list, "Not a list"
    for i in range(len(data)):
        a = random.randint(0,len(data)-1)
        data[i], data[a] = data[a], data[i]
    return data

print("Ex20:", shuffle1([1,2,3,4,5,6,7,8,9,10]))

#Exercise 21
# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).
def typemore():
    a = []
    print("Input anything you want, end with ctrl-d")
    while True:
        try:
            a.append(input())
        except EOFError:
            a.reverse()
            print("Ex21:")
            for line in a:
                print(line)
            return

# typemore()

#Exercise 22
def arrayproduct(ar1=[], ar2=[]):
    assert len(ar1) == len(ar2), "Length must match"
    newarray = []
    for i in range(len(ar1)):
        newarray.append( ar1[i] * ar2[i])
    return newarray

print("Ex22:", arrayproduct([1,2,3,4],[9,8,7,6]))

#Exercise 23

def outofbound(data):
    try:
        data[len(data)+1]
    except IndexError:
        print("Ex23: Don't try buffer overflow attacks in Python!")

outofbound([1,2])


#Exercise 24
def vowelcount(data):
    assert type(data) == str, "Needs to be a string"
    vowel = ['a','i','u','e','o']
    total = 0
    for i in range(len(vowel)):
        total += data.count(vowel[i])
    return total

# Version 2 of vowel
def vowel2(data, vowel = {'a','i','u','e','o'}):
    total = 0
    lowercasedata = data.lower()
    for i in lowercasedata:
        if i in vowel: total += 1
    return total



print("Ex24:", vowelcount("trees"), vowel2("trees"))

#Exercise 25
def removepunctuation(string, punc = {'!','?',',','"',"'",'.'} ):
    Array = list(string)
    for i in Array:
        if i in punc:
            Array.remove(i)
        else:
            continue
    return ''.join(Array)
# Loop the list and check if each Char is in the set. Remove if it sees it. 
# Need to perform this since remove only remove() the first occurences

print("Ex25:", removepunctuation("Do you know? This phrase's uses,a,lot.Of. Punctuation!"))


#Excercise26
def checkformula(a, b, c):
    # a = int(input("a ="))
    # b = int(input('b ='))
    # c = int(input('c ='))
    if a + b == c:
        return True
    elif a == b - c:
        return True
    elif a * b == c:
        return True
    else:
        return False

print("Ex26:", checkformula(2,2,4))

#Exercise27
# In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementations,
# from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance advantages.

def factorgenerator(n):
    for i in range(1,n+1):
        if n % i == 0:
            yield i
        else:
            continue

a = factorgenerator(100)
print("Ex27:", [i for i in a])

# Exercise28
# Euclidean norm, length of vector given 2 coordinates
# Original formula  |v| = (v1^p + v2^p + v3^p) ** 1/p

def norm(v,p=2):
    total = sum([i**p for i in v])
    return total **(1/p)
print("Ex28:", norm([3,4]))
    

#Exercise29
# All string output once
def genstring(n=['c','a','t','d','o','g']):
    all = set()
    return all

print(len(genstring()))