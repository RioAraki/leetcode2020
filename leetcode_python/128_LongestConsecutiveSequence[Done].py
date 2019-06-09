# 2019-01-10: pass
# use set (hash table) to make the look up process O(1)
# find the starting point i by checking if i-1 in the list


def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    set_nums = set(nums)
    
    mx = 0
    for i in nums:
        # we want to find the beginning of streak
        if i-1 not in set_nums:
            streak = 0
            while i in set_nums:
                streak += 1
                i += 1
            mx = max(mx, streak)
    return mx
            