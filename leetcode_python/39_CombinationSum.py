# a top-down approach, might not be efficient enough since we go over every element in the saved data

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

# better bottom-up approach, more efficient

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
            if target - can > 0:
                if not len(dp[target - can]):
                    dp[target - can] = recurSum(target - can, dp)
                for comb in dp[target - can]:
                    if sorted(comb + [can]) not in dp[target]:
                        dp[target].append(sorted(comb + [can]))
        return dp[target]

    return recurSum(target, dp)