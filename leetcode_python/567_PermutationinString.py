def checkInclusion(self, s1: str, s2: str) -> bool:
    s1Cnt = collections.Counter(s1)
    meet = 0
    start,end = 0, 0
    for end in range(len(s2)):
        if s2[end] in s1Cnt:
            s1Cnt[s2[end]] -= 1
            if s1Cnt[s2[end]] == 0:
                meet += 1
        if end >= len(s1):
            if s2[start] in s1Cnt:
                if s1Cnt[s2[start]] == 0:
                    meet -= 1
                s1Cnt[s2[start]] += 1
            start += 1
        if meet == len(s1Cnt):
            return True
    return False