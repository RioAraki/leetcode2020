class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []

        for i in range(1, len(triangle)):
            dp.append([0 for x in range(i)])
        dp.append(triangle[-1])

        def recur(x, y):
            if x < len(triangle) - 1:
                if dp[x][y] == 0:
                    dp[x][y] = triangle[x][y] + min(recur(x + 1, y), recur(x + 1, y + 1))
            return dp[x][y]

        return recur(0, 0)