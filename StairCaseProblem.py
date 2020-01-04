import os

# Stair Case problem
# Write a program where user takes an input
# Based on that input, it will print a stair.
# For example: 3 as input
# Output:
#   #
#  ##
# ###
#
# Above is the output

# Below is my code and solution
# Iterate is firstly used to take the input from user
# then 2 loops which print the space and the bar

# Solutions1
iterate = int(input("Enter Input:"))
def printStairs(iterate):
    for i in range(iterate):
        stairs = i+1
        space = iterate - stairs
        # print('Stairs is: {0} and Space is: {1}'.format(stairs,space))
        for i in range(space):
            print(' ', end='')
        for i in range(stairs):
            print('#', end='')
        print('')


printStairs(iterate)


# Solutions2 on how to do it another way
# levels = int(input())
# for x in range(levels):
#     x = x + 1
#     spaces = ' ' * (levels - x)
#     blocks = '#' * x
#     out_str = (spaces+blocks).rstrip()
#     print(out_str)


# Solutions3 on how to do it another way
# cases = int(input())

# for i in range(1, cases + 1):
#     print((cases - i) * " " + i * "#")    