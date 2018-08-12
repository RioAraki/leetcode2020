from collections import Counter



def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """

    ret = []

    aword = A.split(" ")
    bword = B.split(" ")

    acount = Counter(aword)
    bcount = Counter(bword)

    for i in list(acount - bcount):
        if acount[i] == 1:
            ret.append(i)

    for i in list(bcount - acount):
        if bcount[i] == 1:
            ret.append(i)

    return ret