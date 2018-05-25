class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # Recursion: from start point to each point, find all posible paths
        # Use a 2d array same as size of m*n grid, value in each spot means the possible routes form beginning to that spot.

        def mem(obstacleGrid):
            memo = [[0 for x in range(len(obstacleGrid[0]))] for y in range(len(obstacleGrid))]
            queue = []

        def spot(obstacleGrid, memo, point, queue):
            # check if down valid (is 0 and not out of bound)
            if point[1] + 1 < len(obstacleGrid):
                if obstacleGrid[point[1] + 1][point[0]] == 0:
                    memo[point[1] + 1][point[0]] = memo[point[1]][point[0]] + 1
                else:
                    memo[point[1] + 1][point[0]] = memo[point[1]][point[0]]
                queue.append((point[0], point[1] + 1))

            # check if right valid (is 0 and not out of bound)
            if point[0] + 1 < len(obstacleGrid[0]):
                if obstacleGrid[point[1]][point[0] + 1] == 0:
                    memo[point[1]][point[0] + 1] = memo[point[1]][point[0]] + 1
                elif obstacleGrid[point[1]][point[0] + 1] == 0:
                    memo[point[1]][point[0] + 1] = memo[point[1]][point[0]]
                queue.append((point[0] + 1, point[1]))




