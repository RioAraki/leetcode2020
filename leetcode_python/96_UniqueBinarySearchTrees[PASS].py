# 2018-12-24 Pass


# dp idea, dp[i] is the num of trees when n = i;
# dp[i] = 2 * (dp[i-1] + dp[i-2]*dp[1] + dp[i-3]*dp[2] + ...) 
                                         
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        # initialize, when n = 0, answer is 1
        dp = [0 for i in range(n+1)]
        dp[0],dp[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1,i+1):
                smaller = j-1
                bigger = i-j
                print(i,j,smaller,bigger)
                dp[i] += dp[smaller] * dp[bigger]
        return dp[-1]