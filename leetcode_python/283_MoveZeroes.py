def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    N = len(nums)
    if len(nums) > 1:
        ptr1, ptr2 = 0, 1
        while ptr2 < N:
            if nums[ptr1] == 0 and nums[ptr2] == 0:
                ptr2 += 1
            elif nums[ptr1] == 0 and nums[ptr2] != 0:

                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
                ptr2 += 1
            else:
                ptr1 += 1
                ptr2 += 1
