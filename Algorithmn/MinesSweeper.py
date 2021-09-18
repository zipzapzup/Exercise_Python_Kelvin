def CreateMines(x, y, mines):
    Box = []
    for i in range(y):
        col = []
        for k in range(x):
            col.append(0)    
        Box.append(col)

    print(Box)

CreateMines(3,7, 4)

