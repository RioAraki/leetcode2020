def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    for i in range(n):
        if 0 < nums[i] <= n:
            if nums[i] != i + 1:
                # order matters
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i]-1]
        else:
            nums[i] = 0

    for i in range(n):
        if nums[i] != i+1:
            return i + 1
    return n+1


if __name__ == "__main__":
    nums1 = [1,2,3,4]
    nums2 = [0,3,2,1]
    nums3 = [2,2]
    nums4 = [-3,-2,0,9,1,2]
    nums5 = [1,2,3,4,5,6,9,8]

    test = [nums1, nums2, nums3, nums4, nums5]

    for case in test:
        print(firstMissingPositive(case))