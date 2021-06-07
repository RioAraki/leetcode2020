def minFlips(s: str) -> int:
    size = len(s)
    # two times length of original size, this is used to mimic type1 operation
    desired0 = "01" * size
    desired1 = "10" * size
    diff0 = 0
    diff1 = 0
    minDiff = 99999999
    doubleS = s * 2
    
    for i in range(size):
        if i == 0:
            for j in range(size):
                if s[j] != desired0[j]: diff0 += 1
                if s[j] != desired1[j]: diff1 += 1
        else:
            if doubleS[i-1] != desired0[i-1]: diff0 -= 1
            if doubleS[i+size-1] != desired0[i+size-1]: diff0 += 1
            if doubleS[i-1] != desired1[i-1]: diff1 -= 1
            if doubleS[i+size-1] != desired1[i+size-1]: diff1 += 1
        minDiff = min(minDiff, diff0, diff1)   
    return minDiff