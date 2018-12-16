def maxIncreaseKeepingSkyline(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # found the skyline of two different sides
    # each element have the two constrains which are the two skylines, element could be increased to the min of the two constraints except the element is the skyline itself.
    if not grid: return 0

    maxRow = [max(x) for x in grid]
    maxCol = [max([i[x] for i in grid]) for x in range(len(grid[0]))]
    ret = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < min(maxRow[i], maxCol[j]): ret += min(maxRow[i], maxCol[j]) - grid[i][j]
    return ret


#  Use map to get row and col even quicker (the use of zip(*grid) is brilliant)
#  Once we know row and col, no longer needs to compare it with the grid
def betterMaxIncreaseKeepingSkyline(self, grid):

    rows, cols = list(map(max, grid)), list(map(max, zip(*grid)))
    return sum(min(i,j) for i in rows for j in cols) - sum(map(sum, grid))