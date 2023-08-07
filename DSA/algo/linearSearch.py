# Linear Search

# Search algorithmn to go through all the elements
# Runs in O(n) Time

elements = [2, 3, 5, 6, 7, 8, 9, 10, 20, 27, 30, 40, 48, 50, 100]

def linearSearch(n: list, target: int) -> bool:
    for i in n:
        if i == target:
            return True
    return False


linearSearch(elements, 40) # True
linearSearch(elements, 33) # False