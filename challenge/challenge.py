# O(n) time complexity
def remove_even(lists: list):
    odds = []

    for number in lists:
        if number % 2 != 0:
            odds.append(number)
    return odds

def remove_even2(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0 or lst[i] == 0:
            lst[i:] = lst[i + 1:]
            continue
        i += 1
    return lst







def main():

    inputs = [
            [3, 2, 41, 3, 34],
            [-5, -4, -3, -2, -1],
            [-1, 2, 3, -4, -10],
            [1, 2, 3, 7],
            [2, 4, 6, 8, 10],
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tFinal list: ", remove_even(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()