# C:\Python36

print("This is Kelvin's third script - VarArgs")


# def total(a=5, *numbers, **phonebook, *function2):
#     print('a', a)
#
#     # Iterate through all the items in tuple
#     for single_item in numbers:
#         print('single_item', single_item)
#
#     # Iterate through all items in dictionary
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)
#
#     for i in function2:
#         print i
#
# total(10,1,2,3, Jack=1122, John=2231, Inge=1560, "Jack", "John", "Johhny")


# def multiply(x, y):
#     print(x * y)
#
# multiply(2,3)
#
#
# def supermultiply(*args):
#     a = 1
#     for i in args:
#         a *= i
#     print(a)
#
# supermultiply(3,4,4,2)

def print_kwargs(**kwargs):
    print(kwargs)
    for key, values in kwargs.items():
        print("The value of {} is {}".format(key, values))

print_kwargs(kwargs_1="shark", kwargs_2=4.5, kwargs_3=True)

## Note using a star parameter such as *param, mean that all positional arguments in that point, until the end are collected as a tupleself.
## Note when using 2 star parameter such as **param, then that those arguments are collected as dictionary



## Good example of argument:

def total(a=5, *numbers, **phonebook):
    print('a', a)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))



# # #Output:
# $ python function_varargs.py
# a 10
# single_item 1
# single_item 2
# single_item 3
# Inge 1560
# John 2231
# Jack 1123
# None
