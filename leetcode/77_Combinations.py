# recursion

def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    if k == 0:
        return [[]]

    return [pre + [i] for i in range(k, n + 1) for pre in combine(i - 1, k - 1)]