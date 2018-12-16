def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 0:
        return []

    n = len(nums)
    i = 1
    pre = nums[0]
    while i < n:
        if nums[i] == pre:
            nums.pop(i)
            n -= 1
        else:
            pre = nums[i]
            i += 1
    return nums

# for some reason leetcode accept this solution, the returned value must be int and would be interpret as a list
def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    n = len(nums)
    i = 1
    while i < n:
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            n -= 1
        else:
            pre = nums[i]
            i += 1
    return len(nums)

if __name__ == "__main__":
    nums = [1]
    print(removeDuplicates(nums))