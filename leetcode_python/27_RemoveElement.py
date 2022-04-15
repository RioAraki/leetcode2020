def removeElement(nums: List[int], val: int) -> int:
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while val in nums:
        nums.remove(val)
    return len(nums)

def removeElement2(nums: List[int], val: int) -> int:
    ptr1, ptr2 = 0, len(nums)-1
    while ptr1 <= ptr2:

        if nums[ptr1] == val:
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr2 -= 1
        else:
            ptr1 += 1
    return ptr1

def removeElement3(nums: List[int], val: int) -> int:
    time = len(nums)
    idx = 0
    while time:
        if nums[idx] == val:
            del nums[idx]
        else:
            idx += 1
        time -= 1
    return idx