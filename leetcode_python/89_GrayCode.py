# 2018-12-16: Understand the idea, could redo

# logic:
# recursion
# base pattern: when n = 1 -> b[0,1] -> d[0,1]
# when n increment -> b[00, 01, 11, 10] -> b[0,1,3,2]
    # reverse the old result, add 2**(n-1) to it: [0,1] -> [1 + 2,0 + 2]
    

def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    if n == 0:
        return [0]
    else:
        ret = [0,1]
        for i in range(1, n+1):
            if i > 1:
                pow = 2**(i-1)
                ret = ret + list(map(lambda x: x+pow, ret[::-1]))
    return ret