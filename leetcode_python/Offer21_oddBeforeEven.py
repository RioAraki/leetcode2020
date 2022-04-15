def exchange(nums: List[int]) -> List[int]:
    # two pointer
    # odd odd
    # even even -> ptr2 + 1
    # even odd -> swap
    # odd even -> ptr1 + 1

    if len(nums) <= 1: return nums

    ptr1, ptr2 = 0, 1
    while  ptr2 < len(nums):
        if nums[ptr1] % 2:
            ptr1 += 1
        elif not nums[ptr1] % 2:
            if nums[ptr2] % 2:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
            ptr2 += 1



        if ptr1 == ptr2:
            ptr2 += 1
    return nums