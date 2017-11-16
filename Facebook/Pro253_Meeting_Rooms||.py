'''
Facebook_Medium
11.2 1:29pm
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from queue import PriorityQueue
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        count = 1
        q = PriorityQueue()
        q2 = PriorityQueue()
        for i in intervals:
            q.put((i.start, i.end))
        while not q.empty():
            i = q.get()
            if not q2.empty():
                end = q2.get()
                if i[0] < end:
                    q2.put(end)
                    count += 1
            q2.put(i[1])
        return count