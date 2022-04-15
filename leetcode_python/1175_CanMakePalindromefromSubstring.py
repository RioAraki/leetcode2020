# TLE
import collections
def canMakePaliQueries(s, queries):
    """
    :type s: str
    :type queries: List[List[int]]
    :rtype: List[bool]
    """
    ret = []

    for left, right, substitute in queries:
        tmp = collections.Counter(s[left:right + 1])
        odds = 0
        bit = 0 if len(s[left:right + 1]) % 2 == 0 else 1
        for i in tmp.values():

            if i % 2 == 1:
                odds += 1

                if odds > substitute * 2 + bit:
                    print(substitute * 2 + bit)
                    ret.append(False)
                    break

        else:
            ret.append(True)

    return ret

# Pass 5175 with one simple trick, check if substitute > 13, since we can rearrange and there are only 26 letters
def canMakePaliQueriesPASSED(s, queries):
    """
    :type s: str
    :type queries: List[List[int]]
    :rtype: List[bool]
    """
    ret = []

    for left, right, substitute in queries:
        if substitute > 13:
            ret.append(True)
        else:
            tmp = collections.Counter(s[left:right + 1])
            odds = sum([x % 2 == 1 for x in tmp.values()])

            if odds // 2 <= substitute:
                ret.append(True)
            else:
                ret.append(False)

    return ret