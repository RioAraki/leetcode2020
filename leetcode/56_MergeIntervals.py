# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


import collections


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        # sorted would return a list? Yes, but will not change entries' types
        intervals = sorted(intervals, key=lambda x: x.start)
        ret = [intervals[0]]

        for i in intervals[1:]:
            if i.start <= ret[-1].end:
                ret[-1].end = max(ret[-1].end, i.end)
                ret[-1].end = max(ret[-1].end, i.end)
            else:
                ret.append(i)
        return ret