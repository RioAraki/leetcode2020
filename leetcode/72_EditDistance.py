class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            dp[0][i] = i
        for j in range(len(word2) + 1):
            dp[j][0] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[j][i] = dp[j - 1][i - 1] if word1[i - 1] == word2[j - 1] else min(dp[j - 1][i], dp[j][i - 1],
                                                                                     dp[j - 1][i - 1]) + 1
        return dp[len(word2)][len(word1)]


        # Error 1: index error: dp[j][i] correspond to word[i-1] vs word[j-1] not word[i] vs word[j]
        # Error 2: logic error: the logic when word[i] == word[j] is wrong