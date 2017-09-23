'''
Math_Easy
9.20 12:46pm
'''


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        while True:
            if not num % 2:
                num = num // 2
            elif not num % 3:
                num = num // 3
            elif not num % 5:
                num = num // 5
            else:
                break
        if num == 1 :
            return True
        else:
            return False
