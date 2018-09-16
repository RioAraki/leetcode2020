# why my dfs solution is wrong?


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
            if board[h][w] == word[0]:
                if findNext(board, word, (0,0), 1, (h,w)):
                    return True
    return False


def findNext(board, word, di, idx, pos):
    if idx == len(word):
        print(True)
        return True

    hi, we = len(board), len(board[0])
    neighbor = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # valid neighbor: not going back to direction we come from, not go out of border

    neighbor = list(filter(lambda x: x != di and hi > pos[0] + x[0] >= 0 and we > pos[1] + x[1] >= 0, neighbor))



    for nei in neighbor:

        print(neighbor)
        print(nei, board[nei[0] + pos[0]][nei[1] + pos[1]])
        if board[nei[0] + pos[0]][nei[1] + pos[1]] == word[idx]:
            if findNext(board, word, (-nei[0], -nei[1]), idx + 1, (nei[0] + pos[0], nei[1] + pos[1])):
                return Truex


def dfs(word, gen):
    print(gen)
    if len(gen) <= len(word):
        if gen == word:
            return True
        lst = ["a","b"]
        for i in lst:
            dfs(word, gen+i)
    return False

print(dfs("ba",""))

# def dfs(board, word, i,j):
#     if len(word) == 0:
#         return True
#     if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
#         return False
#     tmp = board[i][j]
#     board[i][j] = "#"
#     res = dfs(board, word[1:], i+1, j) or dfs(board, word[1:], i, j+1) or\
#           dfs(board, word[1:], i-1, j) or dfs(board, word[1:], i, j-1)
#     board[i][j] = tmp
#     return res

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

# print(findNext(board, word, (0,0), 1, (1,1)))
# print(exist(board, word))