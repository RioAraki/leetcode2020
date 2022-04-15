def maximumRemovals(s: str, p: str, removable: List[int]) -> int:
    
    # given the remove list, check if p could be part of s
    def check(remove):
        pIdx = 0
        remove = set(remove)
        for sIdx in range(len(s)):
            if pIdx == len(p):
                return True
            if sIdx in remove:
                continue
            if s[sIdx] == p[pIdx]:
                pIdx += 1
        return pIdx == len(p)
    
    
    lo, hi = 0, len(removable)
    
    while lo < hi:
        mi = (lo + hi)//2
        if check(removable[:mi+1]):
            lo = mi+1
        else:
            hi = mi
    return lo
    
    
