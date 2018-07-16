def binaryGap(self, N):
    """
    :type N: int
    :rtype: int
    """
    binary = str(bin(N)[2:])

    tmp = -1
    ret = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            if tmp != -1:
                ret = max(ret, i - tmp)
            tmp = i
    return ret