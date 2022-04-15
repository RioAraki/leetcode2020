def findAnagrams(self, s: str, p: str) -> List[int]:
    res = []
    if len(s) < len(p): return res
    
    pCnt = collections.Counter(p)
    matched = 0
    
    for end in range(len(s)):
        right = s[end]
        if right in pCnt:
            pCnt[right] -= 1
            if pCnt[right] == 0:
                matched += 1
    # when end >= size of p need to eliminate the left most element in the window to make sure window size always = p
        if end >= len(p):
            left = s[end - len(p)]
            if left in pCnt:
                if pCnt[left] == 0:
                    matched -= 1
                pCnt[left] += 1
                
    # if number of matches == num of char in p, then all chars in p are matched
        if matched == len(pCnt):
            res.append(end-len(p)+1)
    return res