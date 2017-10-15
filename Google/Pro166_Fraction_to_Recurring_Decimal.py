'''
Google_Medium
10.11 3:12pm
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator:
            return '0'

        is_minus = False
        if numerator < 0:
            numerator = 0 - numerator
            is_minus = not is_minus
        if denominator < 0:
            denominator = 0 - denominator
            is_minus = not is_minus

        p1 = numerator // denominator
        ret = ''
        if numerator % denominator:
            p2 = "."
            numerator_set = []
            numerator = numerator % denominator
            while numerator and not numerator in numerator_set:
                numerator_set.append(numerator)
                p2 = p2 + str(numerator * 10 // denominator)
                numerator = numerator * 10 % denominator
            if numerator == 0:
                ret = str(p1) + p2
            else:
                print(numerator_set)
                i = numerator_set.index(numerator)
                # print(p2)
                ret = str(p1) + p2[:i + 1] + '(' + p2[i + 1:] + ')'
        else:
            ret = str(p1)
        if is_minus:
            return '-' + ret
        else:
            return ret