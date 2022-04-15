class Solution:
    
    def rob(self, nums: List[int]) -> int:
        dp = [0 for x in range(len(nums))]
        if len(nums) == 0:
            return 0
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[-1]
        dp[1] = max(nums[0:2])
        if len(nums) <= 2:
            return dp[-1]
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]