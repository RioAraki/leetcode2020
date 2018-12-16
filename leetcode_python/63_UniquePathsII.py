class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # Recursion: from start point to each point, find all posible paths
        # Use a 2d array same as size of m*n grid, value in each spot means the possible routes form beginning to that spot.

        def spot(obstacleGrid, memo, point, queue):
            # check if down valid (is 0 and not out of bound)
            if point[1] + 1 < len(obstacleGrid) and obstacleGrid[point[1] + 1][point[0]] == 0:
                memo[point[1] + 1][point[0]] += memo[point[1]][point[0]]
                if (point[0], point[1] + 1) not in queue:
                    queue.append((point[0], point[1] + 1))

            # check if right valid (is 0 and not out of bound)
            if point[0] + 1 < len(obstacleGrid[0]) and obstacleGrid[point[1]][point[0] + 1] == 0:
                memo[point[1]][point[0] + 1] += memo[point[1]][point[0]]
                if (point[0] + 1, point[1]) not in queue:
                    queue.append((point[0] + 1, point[1]))

        if obstacleGrid[0][0] == 1:
            return 0

        memo = [[0 for x in range(len(obstacleGrid[0]))] for y in range(len(obstacleGrid))]
        memo[0][0] = 1
        queue = [(0, 0)]

        while len(queue) != 0:
            point = queue.pop(0)
            spot(obstacleGrid, memo, point, queue)
        return memo[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

# Error 1: indent error: wrong return indentation in mem function
# Error 2: logic error: if the grid is 1(invalid), should not provide it a value to that spot in memo 2d array
# Error 3: logic error: the new route should be the sum of parent route, not + 1
# Error 4: logic error: forgot to deal with the issue that no point should be visited twice
# Error 5: corner case: make the wrong assumption start point is not end point and must be valid
