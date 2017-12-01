# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from queue import PriorityQueue
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)
        q = PriorityQueue()
        count = 1
        for v in intervals:
            if q.empty():
                q.put(v.end)
            else:
                q.put(v.end)
                peek = q.get()
                if v.start<peek:
                    q.put(peek)
                    count+=1
        return count