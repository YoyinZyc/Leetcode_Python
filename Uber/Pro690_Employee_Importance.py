'''
Uber_Easy
10.31 12:24am
'''
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
from collections import deque


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        d = dict()
        for v in employees:
            d[v.id] = v
        q = deque()
        q.append(d[id])
        ret = 0
        while q:
            e = q.pop()
            ret += e.importance
            for v in e.subordinates:
                q.append(d[v])
        return ret