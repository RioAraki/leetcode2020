# use binary search to find the correct speed of eating


class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        import math
        # search space from 1 to largest in piles
        l, r = 1, max(piles)
        while l < r:
            # m is the temp eating spped, if
            m = (l + r) // 2
            # sum(xxx) are total hour needed for all, if > H, the value m we take is too smaller, increment it by one
            if sum(math.ceil(p/m) for p in piles) > H: l = m + 1
            # r = m to half the search space
            else: r = m
        return l