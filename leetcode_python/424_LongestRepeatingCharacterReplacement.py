import collections

def characterReplacement(s: str, k: int) -> int:
    cnt = collections.Counter()
    left = 0
    res = 0
    
    def isWindowValid():
        return sum(cnt.values()) - max(cnt.values()) <= k
    
    for right in range(len(s)):
        cnt[s[right]] += 1
        
        while not isWindowValid():
            cnt[s[left]] -= 1
            left += 1
        res = max(res, right-left+1)
        
    return res