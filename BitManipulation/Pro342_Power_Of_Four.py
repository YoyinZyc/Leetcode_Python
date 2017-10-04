'''
BitManipulation_Easy
10.4 12:21am
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        s = str(bin(num))
        if s.count('1') == 1 and len(s) % 2 == 1:
            return True
        else:
            return False


