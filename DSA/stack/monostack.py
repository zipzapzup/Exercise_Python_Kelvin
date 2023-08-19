# monotonic stack
# in a decreasing order monotonic stack, the bottom of stack always contains the largest element
# in decreasing order
from collections import deque

temperature = [73, 74, 75, 71, 69, 72, 76, 73]
numbers = [73, 74, 75, 71, 100, 72, 30, 73, 10]

def monotonicStack(array: list):
    stack = deque()

    for i in range(len(array)):
        print(stack)
        while stack and array[i] > stack[-1]:
            stack.pop()
        stack.append(array[i])
        print("largest element", stack[0])

    return stack


a = monotonicStack(temperature)
print(a[0])

b = monotonicStack(numbers)
print(b[0])
