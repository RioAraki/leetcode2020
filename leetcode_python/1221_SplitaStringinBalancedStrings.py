def balancedStringSplit(self, s: str) -> int:
    cnt = 0
    moreLeft = 0
    for i in range(len(s)):
        if s[i] == "L":
            moreLeft += 1
        else:
            moreLeft -= 1
        
        if moreLeft == 0:
            cnt += 1
    return cnt