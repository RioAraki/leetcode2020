# theMap: 2d array representing the map of maze, 0 means walkable, 1 means obstacle
# start coordinate
# end coordinate


# DFS
def solve(maze, start, des):

    def dfs(maze, start, distance):
        dirs = [[0,1], [0,-1], [-1,0], [1,0]]
        for dir in dirs:
            x = start[0] + dir[0]
            y = start[1] + dir[1]
            count = 0
            while (x >= 0 and x< len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 0):
                x += dir[0]
                y += dir[1]
                count += 1
            if (distance[start[0]][start[1]] + count < distance[x-dir[0]][y-dir[1]]):
                distance[x-dir[0]][y-dir[1]] = distance[start[0]][start[1]] + count
                dfs(maze, [x-dir[0], y -dir[1]], distance)


    distance = [[float('inf') for i in maze[0]] for j in maze]
    distance[start[0]][start[1]] = 0
    dfs(maze, start, distance)

    return distance[des[0]][des[1]] if distance[des[0]][des[1]] != float('inf') else float('inf')



if __name__ == "__main__":
    maze = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    start = [0,0]
    des = [4,4]
    print(solve(maze, start, des))


