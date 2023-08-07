# Binary Search
#
# Search Algorithmn 
# to search a target value
# against a sorted elements
# by finding the midpoints of the elements
# O(log n) Time Complexity

elements = [2, 3, 5, 6, 7, 8, 9, 10, 20, 27, 30, 40, 48, 50, 100]


def binarySearch(element: list, target:int, low: int, high: int) -> bool:
    # define the condition where the search fails
    if low > high:
        return False    
    mid = (high + low) // 2

    if target == element[mid]:
        return True
    elif target < element[mid]:
        return binarySearch(element, target, low, mid -1)
    elif target > element[mid]:
        return binarySearch(element, target, mid + 1, high)
    
binarySearch(elements, 8, 0, len(elements)-1) # return True
binarySearch(elements, 52, 0, len(elements)-1) # return False

print(binarySearch(elements, 8, 0, len(elements)-1),
binarySearch(elements, 52, 0, len(elements)-1) )