def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    res = []
    bin = ""
    for i in A:
        bin += str(i)
        res.append(int(bin,2)%5 == 0) 
    return res