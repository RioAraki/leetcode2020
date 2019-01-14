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
    for i in range(len(gas)):
        init = i
        sum = gas[i]-cost[i]
        while sum >= 0:
            i += 1
            
            if i > len(gas)-1:
                i = 0
            # this must be after i > len(gas)-1 condition to deal with the case list length =1    
            if i == init:
                return init          
            sum += gas[i]-cost[i]
    return -1


# key optimization: if start from station A cannot reach station B, any station from A and B cannot reach station B as well (suppose station A is valid or positive)

def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    start = 0
    total = 0
    tank = 0
    
    for i in range(len(gas)):
        tank = tank + gas[i] - cost[i] 
        if tank < 0:
            start = i+1
            total += tank
            tank = 0
    return -1 if total + tank < 0 else start