
def tribonacci(n: int) -> int:
    if n < 2:
        return n 
    dp = [0 for i in range(n+1)]
    dp[1], dp[2] = 1, 1
    
    def getN(n):
        if n > 2 and dp[n] == 0:
            dp[n] = getN(n-1) + getN(n-2) + getN(n-3)
        return dp[n]
    
    getN(n)

    return dp[-1]