# Q1 https://leetcode.com/contest/leetcode-weekly-contest-55/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        # You can  1. buy the stock if you dont have it/ sell stock if you have it
        #          2. do nothing

        #At the end of the i-th day, we maintain cash, the maximum profit we could have if we did not have a share of stock, and hold, the  maximum profit we could have if we owned a share of stock.

        cash, hold = 0, -prices[0]   # 0 -> if we didn't have the stock at the first day/ -prices[0] -> if we buy the stock at the first day
        for day in range(len(prices)):
            cash = max(cash, (hold + prices[day]) - fee)
            hold = max(hold, cash - prices[day])

        return cash

# Q2 https://leetcode.com/contest/leetcode-weekly-contest-55/problems/minimum-ascii-delete-sum-for-two-strings/

# Q3 https://leetcode.com/contest/leetcode-weekly-contest-55/problems/subarray-product-less-than-k/
