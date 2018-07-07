def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    ret = 0

    # find the median index we need, it might be one or two

    med = float(len(nums1) + len(nums2)) / 2
    if med % 1 != 0:
        med = [int(med - 0.5)]
    else:
        med = [int(med - 1), int(med)]

    # create two pointers, one for each array
    # loop through the smallest element of both array. The loop would terminate as long as median is found
    idx = 0
    ptr1 = ptr2 = 0
    while idx <= med[-1]:

        tmp = 0
        if ptr1 > len(nums1) - 1:
            tmp = nums2[ptr2]
            ptr2 += 1
        elif ptr2 > len(nums2) - 1:
            tmp = nums1[ptr1]
            ptr1 += 1
        else:
            if nums1[ptr1] < nums2[ptr2]:
                tmp = nums1[ptr1]
                ptr1 += 1
            else:
                tmp = nums2[ptr2]
                ptr2 += 1
        # print("ptr1,ptr2,idx: ", ptr1, ptr2, idx, tmp)
        if idx in med:
            ret += tmp
        idx += 1

    return ret / len(med)