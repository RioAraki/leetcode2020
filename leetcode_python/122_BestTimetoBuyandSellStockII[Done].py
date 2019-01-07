def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # when there is an incrment of price, you buy it in previous day and sell in the next day
    n = len(prices)
    if not n: return 0
    total = 0
    
    for i in range(1, n):
        if prices[i] > prices[i-1]:
            total += prices[i] - prices[i-1]
    return total