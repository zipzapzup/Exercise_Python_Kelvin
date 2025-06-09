import array

new_array = array.array('f', [1,2,3,4,5])

odd_array = array.array('i', [1,3,5])
even_array = array.array('i', [2,4,6])

integers = array.array('i')
integers = odd_array + even_array


# array - del
del integers[2]

# array - remove find the array and try to remove them O(n)
integers.remove(3)

# array - pop O(1)
integers.pop()

# lists vs array
#
# lists can contain heterogenous type of elements
# list = [1,2, "string", [1,2, True]]
#
# array can only contain a homogenous type of elements.
# new_array = array.array('u', ['a','c','z'])
#
# under the hood
# - arrays are implemented using one pointer
# as a contiguous elements of arrays
#
# - lists on the other hand are implemented
# where all of the elements contains a pointers
# so there are multiple pointers in the list
# these pointers allow list to contain more type
#
# therefore
# array is more efficient in storage as data structure
# list is more flexible

import numpy as np

new_array = np.array([1,2,3])

if __name__ == "__main__":
    print("array")