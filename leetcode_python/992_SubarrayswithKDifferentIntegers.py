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
            # Everytime a new valid window is confirmed, it = old window + one new element
            # so this new window would generate size of new window number of new subarrays
            res += right - left + 1
            right += 1
        return res
    
    return atMostK(nums,k) - atMostK(nums, k-1)