# TLE

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