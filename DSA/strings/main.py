print("Strings")

a = "abcdefg"
print(a[0:2])

b = "12321"
b =int(b)

ord("a")
ord("b")


string = ["ab", "cd", "ef"]

## O(n) Operation
print("".join(string))




def perfectNumber():
    perfectNum = []
    for num in range(1,1000):
        factorial = []
        for i in range(1,num):
            if num % i == 0:
                factorial.append(i)
        if sum(factorial) == num:
            perfectNum.append(num)

    return perfectNum


print(perfectNumber())