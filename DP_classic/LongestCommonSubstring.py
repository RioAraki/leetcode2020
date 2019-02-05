# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

# Input : X = "GeeksforGeeks", y = "GeeksQuiz"
# Output : 5
# The longest common substring is "Geeks" and is of
# length 5.


def LongestCommonSubstring(x,y):

    dp = [[0 for _ in range(len(x)+1)] for _ in range(len(y)+1)]

    mx = 0

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[j+1][i+1] = dp[j][i] + 1
                mx = max(mx, dp[j+1][i+1])
            else:
                dp[j+1][i+1] = 0
    return mx

if  __name__ == "__main__":
    x = "abcefd"
    y = "xxxxbcef"
    print(LongestCommonSubstring(x,y))
