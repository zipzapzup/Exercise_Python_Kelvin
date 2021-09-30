

def countdown(x):
    if (x == 0):
        print("Complete")
        return 
    else: 
        print(x, " - Counting down")
        countdown(x-1)


countdown(5)
