# myanswer: 2d dp, TLE

def longestArithSeqLength(self, A: List[int]) -> int:

    dp = [[["X", 1] for a in A] for b in A]
    
    ret = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            tmp = A[i] - A[j]
            dp[i][j][0] = tmp
            
            max_prev = 0
            for k in range(j):
                if dp[k][i][0] == tmp:
                    max_prev = max(dp[k][i][1], max_prev)
                
            dp[i][j][1] += max_prev
            ret = max(ret, dp[i][j][1])
    return ret+1

