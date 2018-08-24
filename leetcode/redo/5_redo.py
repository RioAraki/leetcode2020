

def longestPalindrome(s):

    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    curMax = ""
    for i in range(len(s)):
        for j in range(len(s)):
            # when len i- len j = 1 or 2, base case
            print(dp)
            if s[i] == s[j]:
                if abs(i-j) == 0: dp[i][j] = 1
                elif abs(i-j) == 1: dp[i][j] = 2
                elif dp[i+1][j-1]: dp[i][j] = 2 + dp[i+1][j-1]
                if dp[i][j] > len(curMax):
                    curMax = s[i:j+1]
    return curMax

if __name__ == "__main__":
    s = "cabac"
    print(longestPalindrome(s))



