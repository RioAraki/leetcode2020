def minCut(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    if not len(s): return -1
    n = len(s)
    # cut[i]: how many cuts necessary for substring s[:i]
    cut = [0 for x in range(n)]
    #
    dp = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):
        mini = i
        for j in range(i+1):
            if (s[j] == s[i] and (j+1 > i-1 or dp[j+1][i-1])):
                dp[j][i] = True
                # when j is 0, no need for any cut, the whole thing is a palindrome
                # else, based on the result of cut with s[j-1], plus 1
                mini = 0 if j == 0 else min(mini, cut[j-1] + 1)
        cut[i] = mini
    return cut[n-1]