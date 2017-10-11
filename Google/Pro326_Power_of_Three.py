'''
Google_Easy
10.9 7:49pm
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_p3 = 3 ** 19
        return n > 0 and not max_p3 % n
