

array = [2,8,5,3,9,4,1]

# InsertionSort Algorithmn
# used to sort array
# step
# 1. compare the current element to the previous element
# 2. if the previous element is bigger
# 3. then swap
# 4. go through until the first list of the element
# O(n^2) Time Complexity
# O(1) Space
def insertSort(n: list) -> None:
    for i in range(1, len(n)):
        current = n[i]
        j = i
        while j > 0 and n[j-1] > current:
            n[j] = n[j-1]
            n[j -1] = current
            j -= 1
    return n


print(array)
print(insertSort(array))


array2 = [18,3,5,19,20,1,16,3,19,28]

print(array2)
print(insertSort(array2))