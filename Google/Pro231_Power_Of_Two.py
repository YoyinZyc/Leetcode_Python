'''
Google_Easy
10.9 10:38pm
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        v = 2 ** 31
        return n > 0 and not v % n
