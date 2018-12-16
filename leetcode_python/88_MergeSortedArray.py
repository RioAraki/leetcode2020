# 2018-12-16 one time pass

def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    real_nums1 = nums1[:m]
    p1 = 0
    p2 = 0
    pm1 = 0
    while p1 < m or p2 < n:
        if p1 == m:
            nums1[pm1] = nums2[p2]
            p2 += 1
        elif p2 == n:
            nums1[pm1] = real_nums1[p1]
            p1 += 1
        elif real_nums1[p1] <= nums2[p2]:
            nums1[pm1] = real_nums1[p1]
            p1 += 1
        elif real_nums1[p1] > nums2[p2]:
            nums1[pm1] = nums2[p2]
            p2 += 1
        pm1 += 1