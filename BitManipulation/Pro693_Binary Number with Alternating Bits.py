'''
BitManipulation_Easy
10.10 6:09pm
'''
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n % 2:
            move_r = n >> 1
            s = str(bin(move_r ^ n))[2:]
            return not '0' in s
        else:
            move_l = n << 1
            s = str(bin(move_l ^ n))[2:]
            return not '0' in s

