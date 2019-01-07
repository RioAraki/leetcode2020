
# tle

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # keep track of the min price
    # then try to find the max price? max price must be after min price found
    if not len(prices): return 0
    
    maxPro = 0
    n = len(prices)
    for i in range(n-1):
        for j in range(i+1,n):
            maxPro = max(maxPro, prices[j] - prices[i])
    return maxPro


# O(n) solution
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
            maxpro = max(maxpro, prices[i] - minprice)

        return maxpro