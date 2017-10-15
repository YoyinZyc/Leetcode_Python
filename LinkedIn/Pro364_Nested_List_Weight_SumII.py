'''
LinkedIn_Medium
10.13 1:25pm
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        value = 0
        q = deque()
        for v in nestedList:
            if v.isInteger():
                value += v.getInteger()
            else:
                q.append(v)

        (level, ret_value) = self.helper(q)
        return value * (level + 1) + ret_value

    def helper(self, q):
        if not q:
            return 0, 0
        value = 0
        q2 = deque()
        while q:
            l = q.pop()
            for v in l.getList():
                if v.isInteger():
                    value += v.getInteger()
                else:
                    q2.append(v)
        (level, ret_value) = self.helper(q2)
        return level + 1, value * (level + 1) + ret_value
