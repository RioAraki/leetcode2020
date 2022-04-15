class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = len([x for x in chips if x % 2 == 1])
        even = len(chips) - odd
        return odd if odd <= even else even