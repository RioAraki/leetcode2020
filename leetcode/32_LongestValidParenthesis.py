class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        dp = [0 for i in range(len(s))]

        left = 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                if left > 0:
                    left -= 1
                    dp[i] = 2 + dp[i - 1]
                    if i - dp[i] >= 0:
                        dp[i] += dp[i - dp[i]]
        return max(dp)

        # Error 1: logic error: the final output dp, the last element is not always the largest since it may not be valid.

