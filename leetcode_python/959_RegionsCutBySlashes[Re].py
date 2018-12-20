# 2018-12-19: pass, 1032 ms
# TODO: this is a good example for disjoint set, redo it with union-find method

# logic: check the size of one element to know the square's size
# create a (3*size) * (3*size) grid
# draw the grid with empty area and lines
# loop through the area, using dfs to draw each region, see how much regions are there
def regionsBySlashes(self, grid):
    """
    :type grid: List[str]
    :rtype: int
    """
    # 0 -> lines; None -> empty; other number -> individual regions
    newGrid = [[None for i in range(len(grid[0])*3)] for j in range(len(grid[0])*3)]
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == " ":
                pass         
            
            elif grid[i][j] == "/":
                newGrid[i*3+2][j*3+0] = 0
                newGrid[i*3+1][j*3+1] = 0
                newGrid[i*3+0][j*3+2] = 0
       
            elif grid[i][j] == "\\":
                newGrid[i*3+0][j*3+0] = 0
                newGrid[i*3+1][j*3+1] = 0
                newGrid[i*3+2][j*3+2] = 0
    
    UP = (-1,0)
    DOWN = (1,0)
    LEFT = (0,-1)
    RIGHT = (0,1)
    color = 1
    
    
    for i in range(len(newGrid)):
        for j in range(len(newGrid)):
            if newGrid[i][j] == None:
                queue = collections.deque()
                newGrid[i][j] = color
                queue.append((i,j))
                
                while len(queue) != 0:
                    
                    cur = queue.popleft()
                    #print(cur)
                    up0, up1 = (sum(x) for x in zip(cur,UP))
                    down0, down1 = (sum(x) for x in zip(cur,DOWN))
                    left0, left1 = (sum(x) for x in zip(cur,LEFT))
                    right0, right1 = (sum(x) for x in zip(cur,RIGHT))
                    #print(up0, up1, down0, down1, left0, left1, right0,right1,len(newGrid))
                    if up0 >= 0 and newGrid[up0][up1] == None:
                        newGrid[up0][up1] = color
                        queue.append((up0, up1))
                    
                    if right1 < len(newGrid) and newGrid[right0][right1] == None:
                        newGrid[right0][right1] = color
                        queue.append((right0, right1))
                    
                    if down0 < len(newGrid) and newGrid[down0][down1] == None:
                        newGrid[down0][down1] = color
                        queue.append((down0, down1))
                        
                    if left1 >= 0 and newGrid[left0][left1] == None:
                        newGrid[left0][left1] = color
                        queue.append((left0, left1))
                
                color += 1
    print(newGrid)
    return color -1