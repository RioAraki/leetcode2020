def distributeCandies(candies, num_people):
    """
    :type candies: int
    :type num_people: int
    :rtype: List[int]
    """
    
    lst = [0 for x in range(num_people)]
    rSum = sum(range(num_people+1))
    rnd = 0
    
    while candies > rSum:
        candies -= rSum
        rSum += num_people **2
        lst = [sum(x) for x in zip(lst, [x+1+rnd*num_people for x in range(num_people)])]
        rnd += 1
    
    idx = 1
    while candies > rnd*num_people + idx:
        lst[idx-1] += rnd*num_people + idx
        candies -= rnd*num_people + idx
        idx += 1
        
    if candies > 0:
        lst[idx-1] += candies
    
    return lst