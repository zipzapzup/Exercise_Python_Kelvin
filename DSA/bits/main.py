## bits manipulation
## bitwise operator can only be performed on integers


## count number of bits in an integer
## bit shift to right 
## use & operation
## O(n) operation, where n is the number of digits
def countBits(x) -> int:
    num = 0
    while x:
        num += x & 1
        x >>= 1
    return num

countBits(10)

## bit shift to the left double the integer value
## 1 shift pushes the binary
## 0010 - 2
## 0100 - 4
def double(x) -> int:
    return x << 1


## bit shift to the right half the integer value
## 1 right shift halfes it
## 0100 - 4
## 0010 - 2
## return to whole number rounded down
## half(7) = 3 
def half(x) -> int:
    return x >> 1


## bit OR
## adds the bits that are 1
## 2 | 1  = 3
def bitor(x,y):
    return x | y


