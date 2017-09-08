# 1. [EASY] Single number
# https://leetcode.com/problems/single-number

# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# 1. List operation
# Algorithm
#
# Iterate over all the elements in nums
# If some number in nums is new to array, append it
# If some number is already in the array, remove it

def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()