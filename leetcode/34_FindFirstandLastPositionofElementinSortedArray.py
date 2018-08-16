# first binary search would find the left bound
# second binary search, by limiting the search space (new lo to hi) and set mid = (lo + hi) / 2 + 1
# make the mid right biased and have the left bound

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lo, hi = 0, len(nums) - 1
    ret = [-1, -1]
    while (lo < hi):
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if nums[lo] != target: return ret
    ret[0] = lo

    hi = len(nums) - 1
    while (lo < hi):
        mid = (lo + hi) // 2 + 1
        if nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid
    ret[1] = hi

    return ret