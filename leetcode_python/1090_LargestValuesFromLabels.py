def largestValsFromLabels(values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
    valDict = []
    
    for i in range(len(values)):
        valDict.append([values[i], labels[i]])
    
    lblCnt = collections.Counter()
    ret = 0
    cur_nums = 0
    valDict.sort(reverse= True)
    for key,value in valDict:
        if cur_nums >= num_wanted:
            break
        if lblCnt[value] < use_limit:
            print(key, value)
            ret += key
            lblCnt[value] += 1
            cur_nums += 1
    return ret