import collections
def subarraysWithKDistinct(nums: List[int], k: int) -> int:
        
    def atMostK(nums, k):
        cnt = collections.Counter()
        res = left = 0
        for right in range(len(nums)):
            if cnt[nums[right]] == 0:
                k -= 1
            cnt[nums[right]] += 1
            while k < 0:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    k += 1
                left += 1
            res += right - left + 1
            right += 1
        return res
    
    return atMostK(nums,k) - atMostK(nums, k-1)