def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    # rotate clockwise 4 times and check if any time matches
    size = len(mat)
    def rotate90(mat):
        res = [[0 for x in range(size)] for y in range(size)]
        for i in range(size):
            for j in range(size):
                res[j][size-i-1]= mat[i][j]
        return res
    
    for i in range(4):
        if mat == target:
            return True
        mat = rotate90(mat)
    return False