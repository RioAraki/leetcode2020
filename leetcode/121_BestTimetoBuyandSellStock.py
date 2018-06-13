class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        minprice = prices[0]
        maxpro = 0

        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i])
            maxpro = max(maxpro, max(0, prices[i] - minprice))

        return maxpro