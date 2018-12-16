
def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    # Recursively find point to possible connected units, always make sure each connected unit has the smallest value
    # use a 2d array with the same size as grid to record smallest path to each number

    def recur(memo, grid, point, queue):
        # check right
        if point[1] + 1 < len(grid[0]):
            if memo[point[0]][point[1] + 1] == 0:
                memo[point[0]][point[1] + 1] += memo[point[0]][point[1]] + grid[point[0]][point[1] + 1]
            else:
                memo[point[0]][point[1] + 1] = min(memo[point[0]][point[1] + 1],
                                                   memo[point[0]][point[1]] + grid[point[0]][point[1] + 1])
            if (point[0], point[1] + 1) not in queue:
                queue.append((point[0], point[1] + 1))

        # check down
        if point[0] + 1 < len(grid):
            if memo[point[0] + 1][point[1]] == 0:
                memo[point[0] + 1][point[1]] += memo[point[0]][point[1]] + grid[point[0] + 1][point[1]]
            else:
                memo[point[0] + 1][point[1]] = min(memo[point[0] + 1][point[1]],
                                                   (memo[point[0]][point[1]] + grid[point[0] + 1][point[1]]))
            if (point[0] + 1, point[1]) not in queue:
                queue.append((point[0] + 1, point[1]))

    memo = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
    memo[0][0] = grid[0][0]
    queue = [(0, 0)]
    while len(queue) != 0:
        point = queue.pop(0)
        recur(memo, grid, point, queue)
    return memo[-1][-1]

    # Error 1: Index error: if point[0]+1 < len(grid) - 1, dont need the `-1`.

# dp solution

def dpMinPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid: return 0
    dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    dp[0][0] = grid[0][0]

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            v, h = -1, -1
            if j - 1 >= 0:
                v = dp[j - 1][i]
            if i - 1 >= 0:
                h = dp[j][i - 1]

            if (v != -1 and h != -1):
                dp[j][i] = min(v, h) + grid[j][i]
            elif (v == -1 and h == -1):
                pass
            else:
                dp[j][i] = max(v, h) + grid[j][i]

    return dp[-1][-1]
