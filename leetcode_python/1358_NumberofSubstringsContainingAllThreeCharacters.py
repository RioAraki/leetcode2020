import collections
def numberOfSubstrings(s: str) -> int:
    cnt = collections.Counter()
    meet = 0
    res = 0
    start = 0
    for end in range(len(s)):
        if cnt[s[end]] == 0:
            meet += 1
        cnt[s[end]] += 1
        while meet == 3:
            res += len(s)-end
            cnt[s[start]] -= 1
            if cnt[s[start]] == 0:
                meet -= 1
            start += 1
    return res