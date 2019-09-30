def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    costList = [abs(ord(x)-ord(y))for (x,y) in zip(s,t)]
    if all(maxCost < i for i in costList):
        return 0
    
    for i in range(len(costList)):
        if i == 0:
            start, end, diff =0, 0, 0
            curSum = costList[0]
        else:
            curSum += costList[i]
            end = i
            
            while curSum > maxCost:
                curSum -= costList[start]
                start += 1
            
            diff = max(diff, end-start)
            
    return diff + 1