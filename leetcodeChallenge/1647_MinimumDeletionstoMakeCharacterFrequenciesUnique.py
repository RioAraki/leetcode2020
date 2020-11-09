# get count of each alphabet, turn it to reverse sorted array 
# make sure idx+1 alway < idx by 1, or 0

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = collections.Counter(s)
        freq = list(cnt.values())
        freq.sort(reverse=True)
        sumBefore = sum(freq)
        for i in range(1, len(freq)):
            if freq[i] >= freq[i-1]:
                freq[i] = freq[i-1] - 1 if  freq[i-1] - 1 > 0 else 0
        sumAfter = sum(freq)
        return sumBefore - sumAfter
        