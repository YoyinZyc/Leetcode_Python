'''
Backtracking_Medium
9.12 4:34pm
'''
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10

        ret = 10
        for i in range(2,n+1):
            x=9
            for j in range(1,i):
                x *= 10-j
            ret += x
        return  ret