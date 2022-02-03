def BubbleSort(data):
    print("current state:", data)
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp 

        print("current state:", data)

print("Bubble Sort:")
BubbleSort([100,50,20,1,2]) 




def MergeSort(data):
    pass