# check if each row, column, square have duplicate

def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for row in board:
        row = list(filter(lambda x: x !='.', row))
        if len(row) != len(set(row)):
            return False

    for i in range(9):
        col = list(filter(lambda x: x!= '.', [j[i] for j in board]))
        if len(col) != len(set(col)):
            return False

    for i in range(1,4):
        for j in range(1,4):
            square = list(filter(lambda x: x!= '.', [board[x][y] for x in range((i-1)*3, i*3) for y in range((j-1)*3, j*3)]))
            if len(square) != len(set(square)):
                return False

    return True


