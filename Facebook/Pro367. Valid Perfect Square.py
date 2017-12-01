class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num == 0 or num == 1:
            return True
        start = 0
        end = num
        while start <= end:
            mid = (start + end) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                start = mid + 1
            else:
                end = mid - 1
        return False
