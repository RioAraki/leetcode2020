# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

# find out the sum of length of nums1 / 2, so we know the index for median
# set two pointers record nums1 and nums2's index, stop when we meet the index recorded before
# deal with the case one is too short, the other is too long



def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    median = (len(nums1) + len(nums2))/2
    if median % 1 == 0:
        median = [int(median-0.5)]
    else:
        median = [int(median-1), int(median)]

    idx = 0
    ptr1 = ptr2 = 0

    # TODO: 现在印象太清楚了，回头再做