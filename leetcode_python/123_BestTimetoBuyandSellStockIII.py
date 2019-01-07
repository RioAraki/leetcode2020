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
                    maxDiff = (maxDiff)
                    dp[l][i] = max(dp[l][i], dp[l][i - 1], prices[i] - prices[j] + dp[l - 1][j])
                    # print (i,j,dp[l][i-1],prices[i]-prices[j]+dp[l-1][j],dp[l][i])
                    # print(dp)
        return dp[-1][-1]

# Error 1: Logic error: Don't get this dp solution by myself
# Error 2: Index error: mixing the row and column
# Error 3: TLE


#=====================#

# Better solution

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0

        k = 2
        dp = [[0 for x in range(len(prices))] for y in range(k + 1)]

        for l in range(1, k + 1):
            tmpMax = dp[l - 1][0] - prices[0]
            for i in range(1, len(prices)):
                dp[l][i] = max(dp[l][i - 1], prices[i] + tmpMax)
                tmpMax = max(tmpMax, dp[l - 1][i] - prices[i])

        return dp[-1][-1]



def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # use the algo. from 121 to find the two dates for first buy and sell, delete the range between two dates
    # use the same algo. and new date list to find the second one
    
    def oneProMax(prices):
        
        
        minPrice = prices[0]
        maxPro = 0
        mindate = 0
        maxdate = 0
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                mindate = i
            
            if prices[i] - minPrice > maxPro:
                maxPro = prices[i] - minPrice
                maxdate = i
        
        new_prices = prices[:mindate] + prices[maxdate+1:]
        
        
        
        
        return profic, new_prices