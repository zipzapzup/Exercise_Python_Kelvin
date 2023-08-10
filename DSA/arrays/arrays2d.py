#2d arrays


class TicTacToe:
    gameEnded = False
    board = None

    def __init__(self, col=3, row=3):
        if self.board is None:
            self.board = [[" "] * col for i in range(row)]
        print("Starting TicTacToe game")
    
    def printBoard(self):
        for i in self.board:
            print(i)
        print("\n") # endlines

    def drawX(self,x,y):
        if x > 2 or y >2:
            raise TypeError("X Y Coordinate cannot exceed 3")
        self.board[x][y] = "X"

    def drawO(self, x,y):
        if x > 2 or y > 2:
            raise TypeError("X Y Coordinate cannot exceed 3")
        self.board[x][y] = "O"
    



game1 = TicTacToe()
game1.printBoard()
game1.drawX(2,1)
game1.drawO(1,1)
game1.drawX(2,2)
game1.drawO(0,0)
game1.printBoard()

# 

def create2DArray(row, col):
    arr = [[0] * row for i in range(col)]
    for i in arr:
        print(i)
    return arr


arr = create2DArray(5,7)



