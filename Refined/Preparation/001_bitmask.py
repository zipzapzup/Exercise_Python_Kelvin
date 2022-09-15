# BitMod in Python

# Bit Calculation in Python is O(1)

# Function to calculate how many 1's in the bit
# We use the BITwise AND to find out number of bits
# 
#

# For Example: 5 = 0000 0101
# 
# 5 = 0000 0101
# 1 = 0000 0001
# ------------- BIT AND
# 1 = 0000 0001
# AND is used for BITMasking
# BITMasking specifies the 1111 that you want

def calculate_num_of_bit(x: int) -> int:
    no_of_bits = 0 # O(1) S
    while x: # O(n) T
        no_of_bits += x & 1 # O(1)
        x >>= 1  # O(1)
    return no_of_bits

#BigO = O(n) Time Complexity (Linear)


# Recap on BIT
# BIT AND: &
# BIT OR: |
# BIT NOT: ~
# BIT XOR: ^

# A) Bit AND &
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 1 = 1
#
# Usage:
# - BitMasking
# To find out how many 1's in the bit
# For example BITAND by (15) to find the 4 lower binary state 0000 1111
# X  - 0101 0001
# 15 - 0000 1111
# -------------- BIT AND
#    - 0000 0001
#
# - Other Usage is to nullify a certain bit range by adding by 0000



# B) Bit OR | 
# 0 | 0 = 0
# 1 | 0 = 1
# 0 | 1 = 1
# 1 | 1 = 1
#
# BitWise OR follows the OR logical table
#
# True OR True = True
# True OR False = True
# False OR True = True
# False OR False = False
#
# Usage:
# - Union to find out how many 1s between two value 
# For example:
# 1111 1100
# 0000 0011
# ------------ BIT OR
# 1111 1111
# 
# We know that all the bits are active or switched on.


# C) BIT XOR ^
# It is a binary operations which perform XOR operations.
# When True meets True, the answer will be false.
#
#
# True XOR False = True
# False XOR True = True
# True XOR True = False
# False XOR False = False
#
# Note in Real world situation, you can use XOR to find out which bits are different.

def bitwise_xor(num: int) -> int:
    # note bitwise XOR itselves makes all to 0
    # True XOR True = False
    # 1 XOR 1 = 0
    return num ^ num

# D) BIT NOT ~
# A Bitwise NOT is a unary operations 
# An operations to only one set of binary to perform a logical negation of every bit
# In python, it will also inverse the positive and negative
# In mathematics, you can use NOT to get the
# inverse relations + 1

def bitwise_not(num: int) -> int:
    # ~5 = -6
    # ~-6 = 7
    # Note the increments + 1 and inverse
    return ~num

# E) BIT Wise Shift Right
# shifts by 1 bit to the right 


def bit_shift_right(num: int) -> int:
    # bitwise >> 1 
    # it will shift the bit to the right
    # and fill 0 at the start
    # in real life it will return number / 2
    # eg: 6 / 2 = 3
    return num >> 1


# F) BIT Wise Shift Left
# shifts by 1 bit to the left

def bit_shift_left(num: int) -> int:
    # bitwise << 1
    # it will shift bit to the left
    # and fill 0 at the end
    # in real life it will double the number * 2
    # eg: 5 * 2 = 10
    return num << 1


def bit_scrape_lowest_binarybit(num: int) -> int:
    # to get the lowest binary digit erased
    # eg
    #   5 = 0000 0101
    #   4 = 0000 0100 BIT AND &
    #     = 0000 0100
    #
    # eg:
    #   4 = 0000 0100
    #   3 = 0000 0011 BIT AND &
    #   0 = 0000 0000
    return num & (num - 1)


def parity_word(word):
    # Parity of a word is to check the bits in the word
    # Need to count whether the bit is even or odd
    # That is parity of a word
    spaces = int.from_bytes(b' ', 'big')
    byte_word = bytes(word, 'utf-8')
    for i in byte_word: # O(n)
        if i == spaces:
            continue
        no_of_bits = 0
        while i: # O(8)
            no_of_bits += i & 1
            i >>= 1
        if no_of_bits % 2 == 0:
            print("Even Bit")
        else:
            print("Odd Bit")


parity_word('hello   ')



#4.1

def parity_word1(x: int) -> int:
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result
    # O(n) where n refers to the bit size of the word. 
    # Note: bin(10)= = '0b1010'
    #       bin(1000000) = '0b11110100001001000000'
    # size of the binary grows the larger the int


def parity_word2(x: int)-> int:
    result = 0
    while x:
        x &= (x - 1)
        result ^= 1
    return result
    # O(k) where k refers to the number of 1's in the bits of the word.
    # x & (x-1) removes the last binary with the 1
    # returns 1 if odd
    # returns 0 if even
    # ^= 1 is a toggler
    
# parity_word1 vs parity_word2 is a huge improvements
# parity_word2 is O(k), where 1 is O(n)
#
# performance wise can be improved


# (11) - 01011
# (10) - 01010 ~ (NOT)
#      - 10101
#               &
#      - 00001

# Note: x & ~(x-1) will return the lowest 1 bit


def swap_bits_42(x, i , j):
    # We want to swap bits position of x
    # lets compare first
    # if its the same then no need to swap

    # If x is 
    # 1010
    # i = 3
    # j = 0
    # You need to & 1 to check whether its turned on or not
    if (x >> i) & 1 != (x >> j) & 1:
        # if its not equal, we need the masking now
        # for these 2 digits at i, j index
        # masking is 1
        # 1 and bit shift to the integer: i, j
        bit_mask = 1 << i | 1 << j
    # we use XOR now, remember that XOR is a flip switch
    # XOR-ing to 1 is a flip and is used to report of
    # whether the bits are even or odd 
    # an odd bit will return 1
    # an even bit will return 0
    #
    # 0 XOR 1 = 1
    # 1 XOR 0 = 1
    # 0 XOR 0 = 0
    # 1 XOR 1 = 0   =THE XOR works here.
    #
    # Note: anything XOR by 1 flips the bit.
    # 
    # x    = 1010
    # mask = 1001
    # XOR
    #      = 0011
    x ^= bit_mask
    return x



def swap_bits(x, i, j ):
    # x is the bits that we want to change
    # i, j is the position
    # Note: that in this operations, x represents the int of the unicode

    if (x >> i) & 1 != (x >> j) & 1:
        mask = (1 << i) |  (1 << j)
        x ^= mask
    return x
# Analysis: x is an integer that represent the unicode or UTF-8 int of a word    
# BigO Time: O(1)
# BigO Space: O(1)


# Write a program that takes a 64 bit unsigned integer and returns the 64-bit unsigned integer consisting of the bits in reverse order
# For example: 100011 -> 110001

def reverse_bits(x: int) -> int:
    reverse_x = 0
    for i in range(63, 0, -1):
        on = (x >> i & 1)
        reverse_x |= ( on << 63 - i)
    return reverse_x

# Analyse x is an integer
# BigO (Time complexity) O(Log(n)), where n is the size of the integers. Reason for this is that as the number of the input grew n, the order of operations in time wise grows smaller. 
# reverse_bits(5) =  3 operations
# reverse_bits(100) = 7 operations
# reverse_bits(2000) = 11 operations


def reduce(x, y ):
    # to reduce, we can use XOR ^
    return x ^ y


def add_one(x):
    # BitWise NOT is an unary operators
    # BitWise not in arithmatic means: y + x = -1
    # In Arithmatics BitWise NOT ~ is: -(x + 1)
    # return - ~x
    # return - -(x + 1)
    # return x + 1
    return - ~x

def subtract_one(x):
    # BitWise not means y = -(x + 1)
    # BitWise NOT ~ is: x + y = -1
    # return ~ -x
    # return -(-x + 1)
    # return x - 1
    return ~ -x


def add_two_number(x, y):
    # BitWise Operations to calculate adding 2 numbers
    # Adding Bits mean if 1 1 = 10
    # 1 0 = 1
    # 0 1 = 1
    # This is so because the Bits is turned to 1
    # To do this we need to establish the concept of carry
    # 
    # carry = find out where there is a carried over
    while y != 0:
        carry = x & y
        # carry refers to the carried over
        x = x ^ y
        # x is the XOR - after the addition
        # however, when 1 1 = 0, then the carry on gets added or shifted to the left
        y = carry << 1
    return x
    # BigO (Time) - O(Log N), where N refers to number that is being placed. It is LogN because the number of calculations refers to the number of bits the number has. It is Log (Base 2) of the number.
    # BigO (Space) - is O(1)

