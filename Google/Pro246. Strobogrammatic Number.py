'''
题意：
判断一个数字翻转180度后是不是还是原来的数字
96；101

思路：
只有6，9，8，1，0能满足
'''
class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        record = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}
        i = len(num) - 1
        while i >= 0:
            if num[i] not in record or record[num[i]] != num[len(num) - 1 - i]:
                return False
            i -= 1
        return True