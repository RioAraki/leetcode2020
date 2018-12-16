# first binary search would find the left bound
# second binary search, by limiting the search space (new lo to hi) and set mid = (lo + hi) / 2 + 1
# make the mid right biased and have the left bound

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if nums == []: return [-1, -1]
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


# Better solution, divide and conquer

def searchRange(self, nums, target):
    def search(lo, hi):
        if nums[lo] == target == nums[hi]:
            return [lo, hi]
        if nums[lo] <= target <= nums[hi]:
            mid = (lo + hi) / 2
            l, r = search(lo, mid), search(mid+1, hi)
            return max(l, r) if -1 in l+r else [l[0], r[1]]
        return [-1, -1]
    return search(0, len(nums)-1)