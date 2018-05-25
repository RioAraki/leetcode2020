class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array
        # loop through the array, pick i each time
        # then pick j = i+1, k = len(nums)-1, if sum is smaller let j+1, bigger let k-1
        # typical 2 pointer counter problem like Q11

        for num in nums:
            new_tar = target - num
