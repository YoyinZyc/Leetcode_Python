'''
Facebook_Hard
10.4 11:55am
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x**n
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, 0 - n)
        elif n % 2:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n // 2)
