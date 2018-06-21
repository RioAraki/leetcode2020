class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        k = 2
        dp = [[0 for x in range(len(prices))] for y in range(k + 1)]

        for l in range(1, k + 1):
            for i in range(1, len(prices)):
                for j in range(i):
                    dp[l][i] = max(dp[l][i - 1], prices[i] - prices[j] + dp[l - 1][j])
        return dp[-1][-1]

# Error 1: Logic error: Don't get this dp solution by myself
# Error 2: Index error: mixing the row and column
