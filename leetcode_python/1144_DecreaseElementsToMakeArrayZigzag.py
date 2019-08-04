
def movesToMakeZigzag(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    odd, even = 0, 0
    n = len(nums)
    
    for i in range(n):
        
        # even index
        if i % 2 == 0:
            left = float('inf') if i - 1 < 0 else nums[i-1]
            right = float('inf') if i + 1 >= n else nums[i+1]
            smaller = min(left, right)
            if nums[i] >= smaller:
                even += nums[i] - (smaller - 1)
            
        
        # odd index
        else:
            left = float('inf') if i - 1 < 0 else nums[i-1]
            right = float('inf') if i + 1 >= n else nums[i+1]
            smaller = min(left, right)
            if nums[i] >= smaller:
                odd += nums[i] - (smaller -1)
        
    return min(odd, even)