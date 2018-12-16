# 18/11/27 not my idea, need to redo 

# it is a really smart answer yet not the fastest
def minIncrementForUnique(A):
    """
    :type A: List[int]
    :rtype: int
    """
    need = ret = 0
    
    for num in sorted(A):
        ret += max(need - num, 0)
        need = max(num + 1, need + 1)
    return ret