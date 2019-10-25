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
