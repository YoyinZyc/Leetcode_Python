'''
LinkedIn_Medium
10.14 5:41pm
'''
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n <= 2:
            return []
        return self.helper(n, 2)

    def helper(self, n, m):
        ret = []
        i = m
        while i >= m and i <= n ** 0.5:
            if not n % i:
                ret.append([i, n // i])
                l = self.helper(n // i, i)
                for v in l:
                    v.insert(0, i)
                    ret.append(v)
            i += 1
        return ret


