# Not my own work, redo
# Traditional and typical dp way to solve the issue
# Get TLE

class Solution:
    def superEggDrop(self, N, K):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        # each row -> egg
        # column -> floor
        dp = [[0 for x in range(K + 1)] for x in range(N + 1)]

        # set up initial, with 0 or 1 floor we only need to try 0 or 1 trials
        for i in range(1, N + 1):
            dp[i][1] = 1
            dp[i][0] = 0

        # with 1 egg and j floors always j trials
        for j in range(1, K + 1):
            dp[1][j] = j

        # fill rest of the entries in table

        for i in range(2, N + 1):
            for j in range(2, K + 1):
                dp[i][j] = 2 ** 31 - 1
                for x in range(1, j + 1):
                    ret = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                    if ret < dp[i][j]:
                        dp[i][j] = ret
        return dp[N][K]


# Change the saved data, now n means number of trial, entries mean floor

class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # 2d array, k -> egg; n -> num of moves(trial); value -> num of floor
        dp = [[0] * (K + 1) for i in range(N + 1)]

        for m in range(1, N + 1):
            for k in range(1, K + 1):
                # if egg breaks, we can check dp[m-1][k-1] floors
                # if egg does not break, we can check [m-1][k] floors

                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: return m