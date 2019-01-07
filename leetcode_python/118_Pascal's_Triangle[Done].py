def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows ==0:
        return []
    
    dp = [[1]]
    if numRows > 1:
        for i in range(1, numRows):
            new = [i+j for i, j in zip(dp[-1]+[0], [0]+dp[-1])]
            dp.append(new) 
        
    return dp