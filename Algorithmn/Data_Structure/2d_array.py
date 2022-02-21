# Create 1D Array

def create_1darray(n):
    array = [0]*n
    return array

def create_1array(n):
    array = []
    for i in range(n):
        array.append(0)
    return array


# Create 2D Array
def create_2darray(col,row):
    newList = [ [0] * col ]* row
    return newList

def create_2darray2(col, row):
    array = []
    array_col = []
    for i in range(col):
        if i == 0:
            array_col.append(1)
        else:
            array_col.append(0)
    
    for i in range(row):
        array.append(array_col)
    return array

create_2darray2(5,2)

# 2D Arrays and 1D Arrays have their own problems
# Accessing 1D Arrays

array1 = [[1,2,3],[5,1,0],[9,9,9]]

# Prints holistically
for i in array1:
    print(i)

# Access Each Value
for i in range(len(array1)):
    for k in range(len(array1[i])):
        print(array1[i][k], end='')

# Accessing 2D Arrays is in the format of
# array[row][col]