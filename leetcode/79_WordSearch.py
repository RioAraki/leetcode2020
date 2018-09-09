def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    # find first first letter in the board  /  O(board)
    # find letter's adjacent for next letter recursively O(word)

    # Corner case: multiple letters found?

    # do dfs?

    hi, we = len(board), len(board[0])

    for h in range(hi):
        for w in range(we):
            if dfs(board, word, h, w):
                return True
    return False


# def findNext(board, word, di, idx, pos):
#     if idx == len(word):
#         return True
#
#     hi, we = len(board), len(board[0])
#     neighbor = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#     # valid neighbor: not going back to direction we come from, not go out of border
#
#     neighbor = list(filter(lambda x: x != di and hi > pos[0] + x[0] >= 0 and we > pos[1] + x[1] >= 0, neighbor))
#     print(neighbor)
#     for nei in neighbor:
#         if board[nei[0] + pos[0]][nei[1] + pos[1]] == word[idx]:
#             findNext(board, word, (-nei[0], -nei[1]), idx + 1, (nei[0] + pos[0], nei[1] + pos[1]))
#     return False

def dfs(board, word, i,j):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    tmp = board[i][j]
    board[i][j] = "#"
    res = dfs(board, word[1:], i+1, j) or dfs(board, word[1:], i, j+1) or\
          dfs(board, word[1:], i-1, j) or dfs(board, word[1:], i, j-1)
    board[i][j] = tmp
    return res

board = [["A", "B"]]


word = "AB"


# print(findNext(board, word, (0,0), 1, (0,1)))
print(exist(board, word))