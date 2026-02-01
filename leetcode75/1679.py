class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sort the list
        # two pointers, one from the beginning, one from the end
        # if sum > k -> move right left a slot
        # if sum < k -> move left right a slot
        # no pointing to the same number -> left != right
        # if found, left + 1 and right - 1 
        nums = sorted(nums)
        left = 0
        right = len(nums)-1
        ret = 0
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                # as if we will no longer use the numbers
                left += 1
                right -= 1
                ret += 1
        return ret



# two pointer的变种，不能用同一个数两次，以及同一组数两次会稍微有些tricky