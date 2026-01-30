# 238. 除了自身以外数组的乘积

from itertools import accumulate
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # keep two product list, one get product from front to end , one get product from end to front

        product_list_front = list(accumulate(nums, operator.mul))
        product_list_back = list(accumulate(nums[::-1], operator.mul))
        
        ret = []

        # 2,3,4,5,6

        # f: 2,6,24,120,720

        # b: 6,30,120,360,720

        for i in range(len(nums)):
            if i == 0:
                ret.append(product_list_back[-2])
            elif i == len(nums)-1:
                ret.append(product_list_front[-2])
            else:
                ret.append(product_list_back[-2-i] * product_list_front[i-1])
        return ret

# accumulate(nums, operator.mul) is equivalent to nums[0] * nums[1] * nums[2] * ... * nums[n-1]

# 没有前后相乘提前cache结果的思路就比较难在On时间里做出来...不算好题目？

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Build prefix products into result
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        # Multiply by suffix products from right
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result