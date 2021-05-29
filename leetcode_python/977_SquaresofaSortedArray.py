def sortedSquares(nums: List[int]) -> List[int]:
    ptr1, ptr2 = 0, len(nums)-1
    res = []
    while ptr1 <= ptr2:
        if abs(nums[ptr1]) >= abs(nums[ptr2]):
            res = [nums[ptr1] ** 2] + res
            ptr1 += 1
        else:
            res = [nums[ptr2] ** 2] + res
            ptr2 -= 1
    return res