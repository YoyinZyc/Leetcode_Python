'''
Top_Interview_Easy
10:12 6:02pm
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        count = 0
        while 5 ** i <= n:
            count += n // 5 ** i
            i += 1
        return count