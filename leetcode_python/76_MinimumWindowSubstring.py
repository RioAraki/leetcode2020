import collections

def minWindow(self, s, t):
    need = collections.defaultdict(int)
    # need is a dict with all char in t as key, nums of char in t appears as value
    for c in t:
        need[c] += 1
    missing = len(t)

    MAX = float('inf')
    a, b = 0, MAX

    i = 0
    for j, c in enumerate(s, 1):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1

        if missing == 0:
            while need[s[i]] < 0:  # Remove unneeded chars from beginning of window
                need[s[i]] += 1
                i += 1

            if j - i < b - a:
                a, b = i, j

            need[s[i]] += 1
            missing += 1
            i += 1

    return '' if b == MAX else s[a:b]


def minWindow2(self, s: str, t: str) -> str:
    tCnt = collections.Counter(t)
    meet = 0
    left, right = 0, 0
    res = float('INF'), -1, -1
    # keep slide window to right by 1 if cur substring does not match condition
    while right < len(s):
        if s[right] in tCnt:
            tCnt[s[right]] -= 1
            if tCnt[s[right]] == 0:
                meet += 1
            # stop when cur window match condition
            if meet == len(tCnt):
                while meet == len(tCnt):
                    # check if cur result is better than best result
                    if res[0] > right - left + 1:
                        res = right - left + 1, left, right
                    # shrink left window until cur substring no longer match confition
                    if s[left] in tCnt:
                        tCnt[s[left]] += 1
                        if tCnt[s[left]] > 0:
                            meet -= 1
                    left += 1
        right += 1
    return "" if res[1] == res[2] == -1 else s[res[1]:res[2] + 1]