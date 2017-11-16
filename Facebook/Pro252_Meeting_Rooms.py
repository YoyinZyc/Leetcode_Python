'''
Facebook_Easy
11.2 12:51pm
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from queue import PriorityQueue
from collections import deque
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        q = PriorityQueue()
        for i in intervals:
            q.put((i.start, i.end))
        i1 = q.get()
        while not q.empty():
            i2 = q.get()
            if i2[0]<i1[1]:
                return False
            i1 = i2
        return True
if __name__ == '__main__':
    q = PriorityQueue()
    if q:
        print(1)
    q2 = deque()
    if q2:
        print(2)

    l = list()
    if l:
        print(3)
    d = dict()
    if d:
        print(4)
    s = set()
    if s:
        print(5)
