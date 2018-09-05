# since we know there are only three numbers to track, we can set the index of the ending for each number and update
# it accordingly.

def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # if nums[i+1] < nums[i], swap their position

    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1

# use counting sort

from collections import Counter

def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # if nums[i+1] < nums[i], swap their position
    cnt = Counter(nums)
    idx = 0
    for i in cnt:
        nums[idx:idx + cnt[i]] = [i] * (cnt[i])
        idx += cnt[i]