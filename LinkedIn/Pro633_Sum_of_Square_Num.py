'''
LinkedIn_Easy
10.12 11:33am
'''
import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = c // 2
        j = c - i
        (square_i, value1) = self.isSquare(i)
        (square_j, value2) = self.isSquare(j)
        if square_i and square_j:
            return True
        while value1 >= 0:
            if value1 ** 2 + value2 ** 2 == c:
                return True
            elif value1 ** 2 + value2 ** 2 > c:
                value1 -= 1
            else:
                value2 += 1
        return False

    def isSquare(self, n):
        if n == 0 or n == 1:
            return True, n
        if n == 2 or n == 3:
            return False, 1
        if n == 4:
            return True, 2
        begin = 2
        end = n // 2
        while end - begin > 1:
            middle = (end + begin) // 2
            middle_square = middle ** 2
            if middle_square == n:
                return True, middle
            elif middle_square < n:
                begin = middle
            else:
                end = middle
        return False, begin