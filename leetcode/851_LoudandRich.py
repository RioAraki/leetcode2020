class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """

        def loudrich(key, dct, quiet, dp):
            if dp[key] == -1:
                dp[key] = quiet[key]
                ret[key] = key
                for val in dct[key]:
                    dp[key] = min(dp[key], loudrich(val, dct, quiet, dp))
                    ret[key] = quiet.index(dp[key])
            return dp[key]

        dct = {}

        for i in range(len(quiet)):
            dct[i] = []

        for rich in richer:
            dct[rich[1]].append(rich[0])

        # save the max `quietness and richer` people for each people
        dp = [-1 for x in range(len(quiet))]
        ret = [0 for x in range(len(quiet))]
        for key in dct:
            loudrich(key, dct, quiet, dp)

        return ret

