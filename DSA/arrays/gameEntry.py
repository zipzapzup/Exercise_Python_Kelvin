class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def getScore(self):
        return self._score
    
    def getName(self):
        return self._name
    
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)
    

class ScoreBoard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, n):
        return self._board[n]
    
    def __str__(self):
        return "\n".join( str(self._board[j]) for j in range(self._n))
    
    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            
            j = self._n - 1
            # since initially we have checked that our score is highest that the last score
            # while loop through the scores until we find it
            # loop whilst on the go
            # since we know our score is in the high score list
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

    