class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(nums):
            n = len(nums)
            i = 0
            while n > 1:
                nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
                n -= 2
                i += 1

        # corner case, if already max permutation return min
        if nums == sorted(nums)[::-1]:
            reverse(nums)

        # 1. reverse numbers
        # 2. from beginning to the end, find next term i < previous term i-1
        # 3. if found, swap the term i with smallest term bigger than i
        # 4. from index 0 to smallest term bigger than i-1, sort
        # 5. reverse

        else:
            reverse(nums)
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    tmp = 2 ** 31 - 1
                    tmp_i = 0
                    for j in range(i):
                        if nums[j] > nums[i]:
                            if nums[j] < tmp:
                                tmp = nums[j]
                                tmp_i = j
                    nums[tmp_i], nums[i] = nums[i], nums[tmp_i]
                    for k in range(1, i):
                        j = k
                        while j > 0 and nums[j] > nums[j - 1]:
                            nums[j], nums[j - 1] = nums[j - 1], nums[j]
                            j -= 1
                    break
            reverse(nums)