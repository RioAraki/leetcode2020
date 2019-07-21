def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    res = 0
    new_list = []
    for i in dominoes:
        if i[0] > i[1]:
            new_list.append((i[1], i[0]))
        else:
            new_list.append((i[0], i[1]))
    cntr = collections.Counter(new_list)
    
    for i in cntr:
        if cntr[i] > 1:
            res += (1 + cntr[i]-1) * (cntr[i]-1) / 2
    return int(res)