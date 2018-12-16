# binary search solution, tle
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if target < nums[0]:
        return 0

    if target > nums[-1]:
        return len(nums)

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] > target:
            hi = mid
        elif nums[mid] < target:
            lo = mid + 1
    return mid

# better solution in this case, find all elements smaller than target
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    return len(list(filter(lambda x: x < target, nums)))

# Binary search does work, its my binary search is not efficient enough
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if target < nums[0]:
        return 0

    if target > nums[-1]:
        return len(nums)

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] > target:
            hi = mid - 1
            if hi >= 0:
                if nums[hi] < target:
                    return hi + 1
            else:
                return 0

        elif nums[mid] < target:
            lo = mid + 1
            if lo < len(nums):
                if nums[lo] > target:
                    return lo
            else:
                return len(nums)
        else:
            return mid