def buddyStrings(self, A: str, B: str) -> bool:
    
    if len(A) != len(B): return False
    diffList = []
    for idx in range(len(A)):
        if A[idx] != B[idx]:
            diffList.append([A[idx], B[idx]])
                             
    if len(diffList) == 0:
        if len(A) == len(set(A)):
            return False
        return True
    elif len(diffList) == 2:
        if diffList[0][0] == diffList[1][1] and diffList[0][1] == diffList[1][0]:
            return True
        return False
    return False