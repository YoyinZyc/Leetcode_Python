'''
BitManipulation_Easy
10.10 8:25pm
'''


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = len(str(bin(num))[2:])
        mask = 2 ** l - 1
        return mask ^ num

