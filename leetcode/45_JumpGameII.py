

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp with number of jumps?
    # 1d array, index i maintains max position with i jump, max position = i+nums[i]  
    # return i as long as i >= len(nums)-1
    if len(nums) <= 1: return 0

    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    selected = 0
    for i in range(0, n):
        for j in range(selected+1, dp[i-1]+1):
            j = n - 1 if j > n - 1 else j
            if j+nums[j] > dp[i]:
                selected = j
                dp[i] = j+nums[j]
        if dp[i] >= n-1:
            return i+1

    return False

test1 = [1,1,1,1,1]
test2 = [1,2,3,4,5]
test3 = [1,3,2,4,5]
test4 = [1,100,1]
test5 = [1]
test6 = [1,2]
test7 = [7,1,2,3,4,5,6,7,8]
print(jump(test7))
