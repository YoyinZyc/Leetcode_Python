'''
DP_Medium
9.20 11:56pm
'''


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        l = [2,3]
        i = 3
        while i < n:
            j = (i+1) // 2
            m = 0
            while j:
                m = max(l[i-j-1] * j,m)
                j-=1
            l.append(m)
            i+=1
        return l[-1]