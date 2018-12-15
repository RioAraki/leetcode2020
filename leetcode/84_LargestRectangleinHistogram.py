# need to review the solution

# 2018-12-08: O(n^2) TLE

def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    
    # tle, 2d dp -> O(n^2) not good
    
    # 2d dp, dp[start point][end point]
    # max choose from dp[start point][end point -1], new row itself and rect with highest weight
    
    if not heights:
        return 0
    
    dp = [[0 for x in heights] for x in heights]
    
    for i in range(len(heights)):
        for j in range(i+1):
            dp_tmp = dp[i-1][j] if j < i else 0
            # i+1, not i
            rect = min(heights[j:i+1])*len(heights[j:i+1]) if j < i else 0
            dp[i][j] = max(dp_tmp, heights[i], rect)
    return max((max(x) for x in dp))
    
# 2018-12-09: solution using stack
