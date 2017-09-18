'''
Math_Easy
9.17 11:01pm
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ''
        while n:
            # if (n-1) 26:
            ret = chr(ord('A')+(n-1)%26) + ret
            # else:
                # ret = 'Z'+ret
            n = (n-1)/26
        return  ret