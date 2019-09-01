def maxDistance(self, grid: List[List[int]]) -> int:
    self.h = len(grid)
    self.w = len(grid[0])
    
    def distEmptyNei(lst, grid, dist):
        ret = set()
    
        for coor in lst:
            x,y = coor[0], coor[1]
            if x-1 >= 0 and grid[x-1][y] == 0:
                ret.add((x-1, y))
                grid[x-1][y] = dist
            if x+1 < self.h and grid[x+1][y] == 0:
                ret.add((x+1,y))
                grid[x+1][y]= dist
            if y-1 >= 0 and grid[x][y-1] == 0:
                ret.add((x,y-1))
                grid[x][y-1] = dist
            if y+1 < self.w and grid[x][y+1] == 0:
                ret.add((x,y+1))
                grid[x][y+1] = dist
        return list(ret)
                
        
    
    def getNum(num, grid):

        ret = []
        for i in range(self.h):
            for j in range(self.w):
                if grid[i][j] == num:
                    ret.append((i,j))
        return ret
    
    curNums = getNum(1, grid)
    dist = 2
    while curNums:
        
        curNums = distEmptyNei(curNums, grid, dist)
        dist += 1
        # print(grid, dist)
    return dist - 3 if dist - 3 != 0 else -1
    