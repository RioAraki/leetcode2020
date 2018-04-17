# 1. https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0, -prices[0]  # the money in my hand if I sell the stock at the first day/ buy the stock at the first day
        
        for i in range(len(prices)):
            cash = max(cash, prices[i]+hold-fee) # you either sell the stock at day i, or do nothing in case you already sold the stock
            hold = max(hold, cash-prices[i]) # either buy the the stock at day i, or do nothing in case you already buy the stock
            # buy does not implement transaction fee
        return cash