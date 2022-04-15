
def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    if len(arr) <= 1:
        return []
    ret = []
    arr.sort()
    minDiff = 999999
    for (x,y) in zip(arr[:-1], arr[1:]):
        diff = y-x
        if diff < minDiff:
            minDiff = diff
            ret = []
            ret.append([x,y])
        elif diff == minDiff:
            ret.append([x,y])
    return ret