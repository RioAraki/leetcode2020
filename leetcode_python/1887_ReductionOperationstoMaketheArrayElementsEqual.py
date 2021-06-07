import collections

def reductionOperations(nums: List[int]) -> int:
    nums.sort()
    cnt = collections.Counter(nums)
    
    isFirst = True
    curToMin = 1
    res = 0
    for i in cnt:
        if isFirst:
            isFirst = False
            continue;
        res += curToMin * cnt[i]
        curToMin += 1
    return res