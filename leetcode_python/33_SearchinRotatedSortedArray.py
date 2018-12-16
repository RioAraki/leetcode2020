# Redo

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # find index where rotate begins
    lo, hi = 0, len(nums) - 1
    while (lo < hi):
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid

    ro = lo;
    lo, hi = 0, len(nums) - 1

    while (lo <= hi):
        mid = (lo + hi) // 2

        # real medium value considering the rotation, smart move here
        realmid = (mid + ro) % len(nums)
        if nums[realmid] == target: return realmid
        if nums[realmid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1