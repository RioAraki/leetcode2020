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
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == target:
                    return sum

                if abs(sum - target) < abs(ret - target):
                    ret = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return ret