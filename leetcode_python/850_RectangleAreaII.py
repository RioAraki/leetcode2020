class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """

        def coor_tran(lst):
            ret = []
            x1, y1, x2, y2 = lst[0], lst[1], lst[2], lst[3]
            for x in range(x1, x2):
                for y in range(y1, y2):
                    ret.append((x, y))
            return ret

        area = 0
        visited = set()

        for rect in rectangles:
            trans = coor_tran(rect)
            for spot in trans:
                if spot not in visited:
                    visited.add(spot)
                    area += 1
        return area % (10 ** 9 + 7)

# TLE

# A bit too complicate to understand the answer, give up for now
# Some new concepts learnt to solve this issue: segment tree, discretization