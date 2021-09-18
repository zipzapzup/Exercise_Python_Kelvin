# Euclid's Algorithmn
# An algorithmn that find the largest common denominator of 2 integers very quickly


def euclid(a, b):
    while (b != 0):
        remainder = a % b 
        a = b
        b = remainder
    return a 
    
# r = // , a = 20, b = 8
# r = 4 , a = 8, b = 4
# r = 0, a = 4, b = 0

print(euclid(20, 8))  # greatest common denominator 4
print(euclid(60, 96)) # greatest common denominator 12
print(euclid(15, 7))