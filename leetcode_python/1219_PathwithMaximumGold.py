def getMaximumGold(self, grid: List[List[int]]) -> int:
    self.visited = set()
    def dfs(i,j):
        if not (0<=i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0 and (i,j) not in self.visited):
            return -math.inf
        self.visited.add((i,j))
        res = grid[i][j] + max(0, max(dfs(i+x, j+y) for x,y in [[-1,0],[1,0],[0,1],[0,-1]]))
        self.visited.remove((i,j))
        return res
    return max(dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])))