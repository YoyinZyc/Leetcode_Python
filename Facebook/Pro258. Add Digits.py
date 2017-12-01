class Solution:
    # 循环解法
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = num % 10
        j = num // 10
        while i + j >= 10:
            i, j = (i + j) % 10, (i + j) // 10
        return i + j
    # 利用整除9
    def addDigits(self, num):
        r = num % 9
        if r != 0 or num == 0:
            return r
        else:
            return 9
    # 考虑如果num是9的情况，所以就先把num-1
    def addDigits(self, num):
        if num == 0:
            return 0
        return (num - 1) % 9 + 1