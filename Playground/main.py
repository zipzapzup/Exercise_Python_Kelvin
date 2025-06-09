

def nested_loop(n: int)-> int:
    sum = 0
    for i in range(n):
        for k in range(n):
            sum += 1
    return sum

def sum(n: int) -> int:
    sum = 0
    for i in range(n):
        sum += i
    return sum

def print_to_five() -> print:
    for i in range(5):
        print(i)

def main():
    print("hello world")

if __name__ == "__main__":
    main()
    print_to_five()
    print("sum: ",sum(10))
    print("nested loop: ", nested_loop(3))