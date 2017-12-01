class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        if x == 1:
            return 1
        begin = 2
        end = x // 2
        while begin <= end:
            mid = (begin + end) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid - 1
            else:
                begin = mid + 1
        return end