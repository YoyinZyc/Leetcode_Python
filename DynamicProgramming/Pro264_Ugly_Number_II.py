'''
DP_Medium
9.20 11:15pm
'''
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1]
        heapq.heapify(l)
        while n-1:
            v = heapq.heappop(l)
            if not v*2 in l:
                heapq.heappush(l, v*2)
            if not v*3 in l:
                heapq.heappush(l, v*3)
            if not v*5 in l:
                heapq.heappush(l, v*5)
            n-=1
        return heapq.heappop(l)