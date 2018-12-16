# My TLE solution

def advantageCount(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    # if any element in A > B[i], put the smallest element in A > B[i]
    # if none element in A > B[i], put smallest element in A
    ret = []
    for i in range(len(B)):
        bigger = list(filter(lambda x: (x - B[i] > 0), A))
        if len(bigger):
            tmp = min(bigger)
            ret.append(tmp)
            A.remove(tmp)
        else:
            ret.append(min(A))
            A.remove(min(A))
    return ret

# Better solution with almost same idea but optimized by using sort and defaultlist


def advantageCount(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    A = sorted(A)
    take = collections.defaultdict(list)
    for b in sorted(B)[::-1]:
        if b < A[-1]: take[b].append(A.pop())
    return [(take[b] or A).pop() for b in B]