def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # dp, saved data: 1d array, len(range(target)), each element reprs all solution sets to that index.
    dp = [[] for i in range(target + 1)]

    def recurSum(target, dp):
        # base case
        if target in candidates:
            dp[target].append([target])
        for can in candidates:
            if target - can > 0 and len(dp[target - can]):
                for comb in dp[target - can]:
                    if sorted(comb + [can]) not in dp[target]:
                        dp[target].append(sorted(comb + [can]))

    for i in range(1, target + 1):
        recurSum(i, dp)
    return dp[-1]
