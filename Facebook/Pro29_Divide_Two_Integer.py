'''
Facebook_Medium
11.05 7:20pm
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor:
            return -1
        if not dividend:
            return 0
        if dividend < 0 and divisor < 0:
            return min(self.helper(0 - dividend, 0 - divisor)[1], 2147483647)
        elif divisor < 0:
            return 0 - min(self.helper(dividend, 0 - divisor)[1], 2147483648)
        elif dividend < 0:
            return 0 - min(self.helper(0 - dividend, divisor)[1], 2147483648)
        return min(self.helper(dividend, divisor)[1], 2147483647)

    def helper(self, dividend, divisor):
        # print(dividend)
        if divisor == 1:
            return (0, dividend)
        if dividend == divisor:
            return (0, 1)
        elif dividend < divisor:
            return (dividend, 0)
        else:
            d1 = dividend
            d2 = dividend >> 1
            d3 = self.helper(d2, divisor)
            c = d3[0] + d3[0] + (d1 - d2 - d2)
            d4 = d3[1] << 1
            if c >= divisor:
                return (c - divisor, d4 + 1)
            else:
                return (c, d4)
