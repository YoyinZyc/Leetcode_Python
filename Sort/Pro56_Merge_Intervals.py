# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda item:item.end)
        i = -1
        j = -2
        while j > (-1- len(intervals)):
            if intervals[j].end >= intervals[i].start:
                if intervals[i].start > intervals[j].start:
                    intervals[i].start = intervals[j].start
                intervals.pop(j)
            else:
                i-=1
                j-=1
        return  intervals
