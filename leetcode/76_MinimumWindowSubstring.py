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