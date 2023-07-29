# functions

def add(a,b):
    return a + b

print(add(2,10))


# nested functions
# can access objects inside the function
def outer(a,b):
    c = "c"
    def inner():
        return a + b + c
    return inner()
# return  "abc"
print(outer("a","b"))



# double
# can modify objects but not reassign
# unless using nonlocal

def double(arr, val):
    def helper():
        # helper func can modify array
        # arr is doubled
        for i, v in enumerate(arr):
            arr[i] *= 2
        
        # nonlocal modify the value
        # val will be doubled
        nonlocal val
        val *= 2
    helper()
    print(arr, val)


double([1,2,3], 10)
        