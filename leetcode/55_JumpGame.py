# same as q45

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) <= 1: return True

    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    selected = 0
    for i in range(0, n):
        for j in range(selected + 1, dp[i - 1] + 1):
            # avoid overflow
            j = n - 1 if j > n - 1 else j
            if j + nums[j] > dp[i]:
                selected = j
                dp[i] = j + nums[j]
        if dp[i] >= n - 1:
            return True

    return False