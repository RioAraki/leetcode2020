# My TLE solution, for loop + two pointers

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3: return []

        ret = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):  # -2 to avoid over loop
            if nums[i] > 0:
                break  # nums[i] > 0 only means from now on there would not be any more valid solutions
            j, k = i + 1, len(nums) - 1
            while j != k:
                if nums[j] + nums[k] == -nums[i]:
                    if [nums[i], nums[j], nums[k]] not in ret:
                        ret.append([nums[i], nums[j], nums[k]])
                    j += 1  # still need to let the loop continues even we find an answer
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return ret

# Same idea, but did more check on duplicate items

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3: return []

        ret = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):  # -2 to avoid over loop
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # nums[i] > 0 only means from now on there would not be any more valid solutions
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:  # check duplicate elements, save a lot of time
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return ret











