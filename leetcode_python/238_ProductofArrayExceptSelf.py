class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        tmp = []
        n = len(nums)
        # 例： [3,4,5,6]
        # 这个loop结束后 tmp 值 [1, 1*3, 1*3*4, 1*3*4*5]
        for i in range(n):
            tmp.append(val)
            val *= nums[i]
        
        val = 1
        # 这个loop结束后 tmp = [1*4*5*6*1, 1*3*5*6*1, 1*3*4*6*1, 1*3*4*5*1]
        for i in range(n-1, -1, -1): # 按照类似 4 3 2 1 的方式倒序
            tmp[i] *= val
            val = val*nums[i]
        return tmpclass Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        tmp = []
        n = len(nums)
        # 例： [3,4,5,6]
        # 这个loop结束后 tmp 值 [1, 1*3, 1*3*4, 1*3*4*5]
        for i in range(n):
            tmp.append(val)
            val *= nums[i]
        
        val = 1
        # 这个loop结束后 tmp = [1*4*5*6*1, 1*3*5*6*1, 1*3*4*6*1, 1*3*4*5*1]
        for i in range(n-1, -1, -1): # 按照类似 4 3 2 1 的方式倒序
            tmp[i] *= val
            val = val*nums[i]
        return tmp