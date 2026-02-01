# 334. 递增的三元子序列

class Solution:
    def smallest_front_to_end(self, nums: List[int]) -> List[int]:
        # 2 1 5 0 4 6
        # 2 1 1 0 0 0 <- another layer of intermediate list to keep track minimum front to end
        # that's clearly o(n)
        ret = []
        cur_min = 2**31
        for num in nums:
            if num <= cur_min:
                ret.append(num)
                cur_min = num
            else:
                ret.append(cur_min)
        return ret

    def biggest_end_to_front(self, nums: List[int]) -> List[int]:
        # 2 1 5 0 4 6
        # 6 6 6 6 6 6 <- another layer of intermediate list to keep track minimum front to end
        # that's clearly o(n)
        ret = []
        cur_max = -2**31
        nums.reverse()
        for num in nums:
            if num >= cur_max:
                ret.append(num)
                cur_max = num
            else:
                ret.append(cur_max)
        nums.reverse()
        ret.reverse()
        return ret

    def bigger_than(self, nums: List[int]) -> List[bool]:
        # 2 1 5 0 4 6
        # 6 6 6 6 6 6 <- another layer of intermediate list to keep track minimum front to end
        # t t t f t f <- is ther a number x after cur index, such that x > nums[idx] 
        big_list = self.biggest_end_to_front(nums)

        ret = []
        for i in range(len(nums)):
            ret.append(nums[i] < big_list[i])     
        return ret

    def smaller_than(self, nums: List[int]) -> List[bool]:
        # 2 1 5 0 4 6
        # 2 1 1 0 0 0 <- another layer of intermediate list to keep track minimum front to end
        # f f t f t t <- is there a number x before cur index, such that x < nums[idx]
        # BRUTE FORCE ? -> O(n**2)

        small_list = self.smallest_front_to_end(nums)
        ret = []
        for i in range(len(nums)):
            ret.append(nums[i] > small_list[i])
        return ret

    def increasingTriplet(self, nums: List[int]) -> bool:
        # 2 1 5 0 4 6
        # f f t f t t <- is there a number x before cur index, such that x < nums[idx]
        # t t t f t f <- is ther a number x after cur index, such that x > nums[idx]  
        # as long as there is an idx have both true for the above two list, we got a solution
        smaller_than_bool_list= self.smaller_than(nums)
        bigger_than_bool_list = self.bigger_than(nums)

        for i in range(len(nums)):
            if smaller_than_bool_list[i] and bigger_than_bool_list[i]:
                return True
        return False

# 我的思路是找中间值，导致必须遍历数组提前找最大和最小，会不效率
# 如果找最大值，track 最小和第二小，会简单很多
