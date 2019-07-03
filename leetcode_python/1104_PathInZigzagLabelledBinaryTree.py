def pathInZigZagTree(self, label):
    """
    :type label: int
    :rtype: List[int]
    """
    def recur(label, result):
        if label == 1:
            result = [label] + result
            return result
        else:
            lvl = int(math.log(label, 2))   
            prev = label//2
            prev = 2**(lvl-1) + (2**lvl-1 - prev)
            return recur(prev, [label]+result)
            
    return recur(label, [])