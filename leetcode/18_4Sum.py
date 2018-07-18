# The solution based on 2 sum

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 3):

            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: break
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target: continue
            for j in range(i + 1, n - 2):
                # print(i,j)
                if j > i + 1 and nums[j] == nums[j - 1]: continue  # key here, think again about why j > i+1
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target: continue
                l, r = j + 1, n - 1
                # print(nums,i,j,l,r)
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        ret.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[
                            l - 1]:  # failed in this part, l should be compared with l - 1 not l + 1 because l has already been moved and need to compare with previous one
                            l += 1
                        r -= 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
        return ret

# Made several mistakes during implementing the algorithm, need to **redo**