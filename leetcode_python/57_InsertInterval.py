class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    # start at beginning
    # start in the middle
    # in the range of an existed interval
    # in the gap of two intervals
    # start in the end

    # same for end

    # A lot of corner case

    idx = 0

    for i in range(len(intervals)):
        if intervals[i].end >= newInterval.start:
            # start is in the gap between two , in beginning
            if intervals[i].start > newInterval.start:
                intervals.insert(i, newInterval)
            # dont need an extra interval if intervals[i].start < newInterval.start
            idx = i
            break
    # for loop has ended and newInterval always > intervals
    else:
        return intervals + [newInterval]

    dele = []
    newEnd = max(intervals[idx].end, newInterval.end)
    for i in range(idx + 1, len(intervals)):
        if intervals[i].start <= newInterval.end:
            dele.append(i)
            if intervals[i].end > newInterval.end:
                newEnd = intervals[i].end
    intervals[idx].end = newEnd
    for i in dele[::-1]:
        intervals.remove(intervals[i])
    return intervals


# better solution

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        # we are sure i wont be affected by newinterval if newinterval.start > i.end or n.end < i.start
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        # when newinterval.start < i.end, and newinterval.end > i.start,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [Interval(s, e)] + right
