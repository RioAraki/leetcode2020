def numRollsToTarget(d: int, f: int, target: int) -> int:
    # dp(d = dice #, f = face #, target = cur target sum) = dp(d,f,t-1) + ... + dp(d,f,t-6)
    
    # (key = (d,f,t): value = total possiblities)
    dp = {}
    
    def dfs(d,f,target):
        
        # base case
        if d == 1:
            if 0 < target <= f:
                return 1
            else:
                return 0
        
        
        
        if (d,f,target) in dp:
            return dp[(d,f,target)]
        
        curSum = 0
        for i in range(1, f+1):
            curSum += dfs(d-1,f,target-i)
        dp[(d,f,target)] = curSum
        
        return curSum
    
    ret = dfs(d,f,target)
    

    return ret % (10**9 + 7)
    
        
        