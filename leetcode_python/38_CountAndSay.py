def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 0:
        return ""

    def nxtCountAndSay(n):
        ret = ""
        count = 0
        prev = n[0]
        for i in n:
            if i != prev:
                ret += str(count) + prev
                prev = i
                count = 0
            count += 1
        return ret + str(count) + i

    ret = "1"
    for i in range(n - 1):
        ret = nxtCountAndSay(ret)
    return ret

import re
# Use regular expression, or itertools.groupby

# '(.)\1*' -> () capture group, . any char except newline
def reCountAndSay(n):
    s = "1"
    for _ in range(n-1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s