def numSpecialEquivGroups(self, A):
    """
    :type A: List[str]
    :rtype: int
    """

    def SES(A, B):
        if len(A) != len(B) or set(A) != set(B):
            return False
        Aodd, Aeven, Bodd, Beven = [], [], [], []

        for i in range(len(A)):
            if i % 2 == 0:
                Aeven.append(A[i])
                Beven.append(B[i])
            else:
                Aodd.append(A[i])
                Bodd.append(B[i])
        return sorted(Aodd) == sorted(Bodd) and sorted(Aeven) == sorted(Beven)

    # loop each string
    # try to exchange every 1-3 5-7 / 2-4 6-8 pair of index and see if result after loop is in A
    # if in A put them in same group, delete all list from A to prevent duplicate check  visited = []

    ret = []
    for i in range(len(A)):
        if not any([A[i] in x for x in ret]):
            tmp = [A[i]]
            for j in range(i + 1, len(A)):
                if SES(A[i], A[j]):
                    tmp.append(A[j])
            ret.append(tmp)
    return len(ret)

if __name__ == "__main__":
    test = ["couxuxaubw", "zsptcwcghr", "kkntvvhbcc", "nkhtcvvckb", "crcwhspgzt"]
    for i in range(len(test)):
        for j in range(i+1, len(test)):
            print(test[i], test[j], SES(test[i],test[j]))