
'''
Amazon_Medium
10.9 11:44am
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        else:
            l = self.grayCode(n - 1)
            i = len(l) - 1
            while i >= 0:
                l.append(2 ** (n - 1) + l[i])
                i -= 1
            return l


