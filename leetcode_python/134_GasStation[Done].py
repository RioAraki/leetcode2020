# 2019-01-14 pass
# set a balance, if positive this could be a start station, we try to walk through and see if the sum always >= 0

def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    if not gas:
        return 0
    balance = list(map(lambda x,y:x-y,gas,cost))
    for i in range(len(balance)):
        init = i
        sum = balance[i]
        while sum >= 0:
            i += 1
            
            if i > len(gas)-1:
                i = 0
            # this must be after i > len(gas)-1 condition to deal with the case list length =1    
            if i == init:
                return init          
            sum += balance[i]
    return -1