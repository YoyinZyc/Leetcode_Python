'''
Greedy_Medium
9.12 11:04am
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        count = 0
        intervals.sort(key = lambda x: x.end)
        i = 1
        end = intervals[0].end
        while i < len(intervals):
            if intervals[i].start < end:
                count+=1
            else:
                end = intervals[i].end
            i+=1
        return count