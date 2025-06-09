def permutate(string, step=0):
    a = list(string)
    if len(a) == 0:
        print('not possible')
    for i in range(step, len(a)):
        a[i], a[step] = a[step], a[i]
        print(a)





permutate("123")


def permutate1(string, step=0):
    if step == len(string):
        print( "".join(string))
    for i in range(step, len(string)):
        string_copy = list(string) # 123 = 123
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step] #123 = 123.
        #132 = 132 
        permutate(string_copy, step +1)


