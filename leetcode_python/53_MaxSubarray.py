# loop through the list
# if the next element i > current sum + i,let i = new current sum
# if the next element i < current sum + i, current sum = current sum + i
# always record the current highest

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    largest = cur = nums[0]
    for i in nums[1:]:
        cur = max(i, cur + i)
        largest = max(cur, largest)
    return largest