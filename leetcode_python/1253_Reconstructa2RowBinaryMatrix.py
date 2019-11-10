class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        # dfs
        if upper + lower != sum(colsum):
            return []
        
        if len([x for x in colsum if x != 0]) < max(upper, lower):
            return []
        
        ret = [[0 for x in range(len(colsum))],[0 for x in range(len(colsum))]]
        
        for i in range(len(colsum)):
            if colsum[i] == 2:
                upper -= 1
                lower -= 1
                ret[0][i] = 1
                ret[1][i] = 1
                colsum[i] = 0
        
        for i in range(len(colsum)):
            if colsum[i] == 1:
                if upper > 0:
                    upper -= 1
                    ret[0][i] = 1
                else:
                    lower -= 1
                    ret[1][i] = 1
        return ret
        