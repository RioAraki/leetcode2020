# find largest rectangle (border all filled) in given grid. 1 means the grid filled; 0 means it is empty.


def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
    largest = 0
    
    row_list = []
    col_list = []
    
    width = len(grid[0])
    height = len(grid)
    
    
    for j in range(height):
        start = 0
        row_start, row_end = 0, 0
        for i in range(width):
            if grid[j][i] == 1 and start == 0:
                row_start = i
                start = 1
            elif grid[j][i] == 0 and start == 1:
                row_end = i-1
                start = 0
                row_list.append([(j,row_start), (j,row_end)])
        if start == 1:
            row_list.append([(j,row_start), (j,width-1)])
    

    
    for j in range(width):
        start = 0
        col_start, col_end = 0, 0
        for i in range(height):
            if grid[i][j] == 1 and start == 0:
                col_start = i
                start = 1
            elif grid[i][j] == 0 and start == 1:
                col_end = i-1
                start = 0
                col_list.append([(col_start, j), (col_end, j)])
        if start == 1:
            col_list.append([(col_start, j), (height-1, j)])

    largest = 0
    
    for i in range(len(row_list)):
        for j in range(i, len(row_list)):
            r1, r2 = row_list[i]   
            r1x, r1y = r1
            r2x, r2y = r2
            r3, r4 = row_list[j]
            r3x, r3y = r3
            r4x, r4y = r4
            if r1y == r3y and r2y == r4y:
                if r3x - r1x == 0:
                    largest = r2y - r1y + 1 if r2y - r1y + 1 > largest else largest
                else:
                    if [(r1x, r1y),(r3x,r3y)] in col_list and [(r2x, r2y), (r4x, r4y)] in col_list:
                        area = (r2y - r1y + 1) * (r3x-r1x+1)
                        largest = area if area > largest else largest
    return largest