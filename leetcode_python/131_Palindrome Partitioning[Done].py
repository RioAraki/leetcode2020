def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    def isPalindrome(s):
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
    
        return True
    
    
    if not len(s):
        return []
    
    dp = [[] for i in range(len(s))]
    dp[0] = [[s[0]]]
    
    for i in range(1,len(s)):
        dp[i] = [x+[s[i]] for x in dp[i-1]]
        
        for j in range(i-1,-1,-1):
            if isPalindrome(s[j:i+1]):
                if j-1 < 0:
                    dp[i].append([s[j:i+1]])
                else:
                    [dp[i].append(y) for y in [x+[s[j:i+1]] for x in dp[j-1]]]
    return dp[-1]