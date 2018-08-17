# check if each row, column, square have duplicate

def isValidSudoku(board):
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


# string recording: iterate through each element in the sudoku, use three ways to record each value and
# check if anytime duplicate is found

# though it only requires one full loop, the int-to-str process actually takes some time and the overall performance
# is worse than first solution
def betterIsValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    seen = set()

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                tmp = "(%s)" % board[i][j]
                if tmp + str(i) in seen or str(j) + tmp in seen or str(i // 3) + tmp + str(j // 3) in seen:
                    return False
                seen.add((tmp + str(i)))
                seen.add(str(j) + tmp)
                seen.add(str(i // 3) + tmp + str(j // 3))
    return True