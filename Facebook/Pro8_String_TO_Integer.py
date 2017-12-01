import sys


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 看str是不是空
        if not str:
            return 0
        i = 0
        # 去除开始的空格，数字里面不能有空格
        while i < len(str) and str[i] == ' ':
            i += 1
        if i == len(str):
            return 0
        str = str[i:]

        # 去除结尾的空格
        i = len(str) - 1
        while i >= 0 and str[i] == ' ':
            i -= 1
        str = str[0:i + 1]

        print(str)
        # 调整正负号
        if str[0] == '+':
            return min(self.helper(str[1:])[1], 2147483647)
        if str[0] == '-':
            return max(0 - self.helper(str[1:])[1], -2147483648)
        return max(min(self.helper(str)[1], 2147483647), -2147483648)

    def helper(self, str):
        # 如果str为空或者有非数字的字符，返回0
        if not str or not str[0].isdigit():
            return (0, 0)
        # length是用来标识乘到第几位了，一定要从头向后，因为如果遇到空格就停了
        if str[0].isdigit():
            if len(str) == 1:
                return (1, int(str))
            (length, value) = self.helper(str[1:])
        return (length + 1, int(value + int(str[0]) * (10 ** length)))