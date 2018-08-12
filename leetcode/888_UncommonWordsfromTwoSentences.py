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

 def betterUncommonFromSentences(self, A, B):
        # string comprehension, make them all together, then split
        # we dont need to care about uncommon word is from A or B since
        # it will be uncommon if it overall only appears once
        c = Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]