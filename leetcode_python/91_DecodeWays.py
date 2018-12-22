# idea:
# find all possible subset's with length 1 or 2. If its 2 and > 26, discard it

# corner case:
# 0 is a digit,"0", "00", "01" is invalid, but "10" is valid

def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    if not len(s): return 0
    
    ret = [[s[0]]]
    for i in range(1,len(s)):
        n = len(ret)
        for j in range(n):
            if len(ret[j][-1]) == 1:
                ret.append(ret[j]+[s[i]])
                ret[j][-1] = ret[j][-1]+s[i]
            elif len(ret[j][-1]) == 2:
                ret[j].append(s[i])
    invalid = 0
    for lst in ret:
        for num in lst:
            if int(num[0]) == 0 or int(num) == 0 or int(num) > 26:
                invalid +=1
                break

    return len(ret) - invalid