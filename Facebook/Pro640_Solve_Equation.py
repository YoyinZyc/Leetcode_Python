'''
Facebook_Medium
11.05 11:46pm
'''
class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        # 记录x的个数
        x = 0
        num = 0
        # operator 和 d是为了方便设置下一个数是加还是减
        operator = True
        d = {'+': True, '-': False}

        # 记录x的系数 temp
        coefficient = 0
        # 到x的时候判断前面有没有系数
        has_co = False
        # 是不是左边
        isLeft = True
        for v in equation:
            if v == 'x':
                if not has_co:
                    coefficient = 1
                # 在式子的左边
                if operator:
                    x += coefficient
                else:
                    x -= coefficient
                has_co = False
                coefficient = 0
            elif v == '+' or v == '-':
                if coefficient:
                    if operator:
                        num += coefficient
                    else:
                        num -= coefficient
                    coefficient = 0
                    has_co = False
                if isLeft:
                    operator = d[v]
                else:
                    operator = not d[v]
            elif v == '=':
                # 系数要变成常数了
                if coefficient:
                    if operator:
                        num += coefficient
                    else:
                        num -= coefficient
                    coefficient = 0
                    has_co = False
                isLeft = False
                operator = False
            else:
                # 对于是数字的情况，就压入coefficient
                coefficient = 10 * coefficient + int(v)
                has_co = True
        # 跳出循环后还要考虑最后一个会不会是系数
        if coefficient:
            if operator:
                num += coefficient
            else:
                num -= coefficient
        # 如果没有数字也没有x
        if not num and not x:
            return "Infinite solutions"
        # 如果只有数字
        elif not x:
            return "No solution"
        # 如果数字，x都有
        else:
            return 'x=' + str(0 - num // x)