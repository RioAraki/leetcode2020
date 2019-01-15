# 2019-01-14： check the ratings ascending/descending order and assign the value accordingly

def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    if not ratings:
        return 0
    des = []
    asc = []
    ret = [1 for x in ratings]
    n = len(ratings)
    des_s = des_e = asc_s = asc_e = -1
    
    for i,j in zip(range(n-1), range(1,n)):
        # print(i,j)
        if ratings[i] > ratings[j]:
            if asc_s != -1:
                asc.append((asc_s, asc_e))
                asc_s = asc_e = -1
            if des_s == -1:
                des_s, des_e = i, j
            else:
                des_e = j
                
        elif ratings[i] < ratings[j]:
            if des_s != -1:
                des.append((des_s, des_e))
                des_s = des_e = -1
            if asc_s == -1:
                asc_s, asc_e = i, j
            else:
                asc_e = j
        else:
            if asc_s != -1:
                asc.append((asc_s, asc_e))
                asc_s = asc_e = -1
            elif des_s != -1:
                des.append((des_s, des_e))
                des_s = des_e = -1
                
    # last descending/ ascending pair may be missed to be appended            
    if asc_s != -1:
        asc.append((asc_s, asc_e))
    if des_s != -1:
        des.append((des_s, des_e))
        
    for pair in asc:
        start = pair[0]
        end = pair[1]
        for idx, i in enumerate(range(1,end-start+2)):
            ret[start+idx] = max(i, ret[start+idx])
            
    for pair in des:
        start = pair[0]
        end = pair[1]
        for idx, i in enumerate(range(end-start+1,0,-1)):
            ret[start+idx] = max(i, ret[start+idx])

    return sum(ret)


# same idea, better solution:

def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    if not ratings:
        return 0

    ret = [1 for x in ratings]
    n = len(ratings)
    
    for i,j in zip(range(n-1), range(1,n)):
        if ratings[i] < ratings[j]:
            ret[j] = ret[i] + 1
    for i,j in zip(range(n-1,0,-1), range(n-2,-1,-1)):
        if ratings[i] < ratings[j]:
            ret[j] = max(ret[j], ret[i] + 1)
    return sum(ret)
            