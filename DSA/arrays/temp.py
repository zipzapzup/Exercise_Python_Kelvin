from collections import deque
temperatures = [73,74,75,71,69,72,76,73]


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    i = 0
    while i < len(temperatures) - 1:
        k = i + 1
        while k < len(temperatures):
            if temperatures[k] > temperatures[i]:
                temperatures[i] = k - i
            elif k == len(temperatures):
                temperatures[i] = 0
            else:
                k += 1
                continue
            k += 1
        i += 1
    return temperatures

print(dailyTemperatures(temperatures))


def dailyTemp(temperatures):
    stack = deque()
    for i, value in enumerate(temperatures):
        stack.append((i, value))
    
    for i in range(len(temperatures)):

