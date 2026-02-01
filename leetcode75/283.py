# 283. 移动零

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 不动数组本身，感觉又得双指针？
        # 把非零元素往前挪？ O n^2？是否有些brute force
        # 不对还是双指针
        cur_0_index = []

        for i in range(len(nums)):
            # record the index of 0
            if nums[i] == 0:
                cur_0_index.append(i)

            # if nums[idx] is not 0, we should move it with the first 0 pos
            else:
                if len(cur_0_index) == 0:
                    # the non zero number is already at correct place, do nothing
                    pass
                else:
                    # swap the cur num pos with first 0's position
                    first_0 = cur_0_index.pop(0)
                    nums[first_0], nums[i] = nums[i], nums[first_0]
                    cur_0_index.append(i)

        return nums

# 比较平平无奇