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