def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if not rowIndex: return [1]
    
    dp = [1]
    
    for i in range(rowIndex):
        new = [i+j for i, j in zip(dp+[0], [0]+dp)]
        dp = new
    return dp