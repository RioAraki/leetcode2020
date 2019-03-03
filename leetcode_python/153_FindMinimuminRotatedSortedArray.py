def findMin(self, nums: List[int]) -> int:
    if len(nums) == 0: return
    elif len(nums) == 1: return nums[0]
    elif len(nums) == 2: return min(nums)
    
    mid = len(nums) // 2
    
    if nums[mid] < nums[0]:
        return self.findMin(nums[:mid+1])
    
    elif nums[mid] > nums[-1]:
        return self.findMin(nums[mid:])
        
    else:
        return nums[0]
        