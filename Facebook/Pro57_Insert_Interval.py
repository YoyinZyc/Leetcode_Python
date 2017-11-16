'''
Facebook_Hard
11.10 8:09pm
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            i += 1

        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            intervals.pop(i)
        intervals.insert(i, newInterval)
        return intervals