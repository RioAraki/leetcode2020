# pass

def relativeSortArray(self, arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    # built a counter, convert arr1 to this counter
    cntr1 = collections.Counter(arr1)
    
    
    # loop through arr2, check how many copies each numbers has
    set2 = set(arr2)
    
    newList = []
    for i in arr1:
        if i not in set2:
            newList.append(i)
    
    newList.sort()
    

    ret = []
    for i in arr2:
        ret = ret + [i] * cntr1[i]
    
    return ret + newList