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
        x = 0
        num = 0
        operator = True
        d = {'+': True, '-': False}
        coefficient = 0
        has_co = False
        isLeft = True
        for v in equation:
            # print(num)
            # print(x)
            if v == 'x':
                if not has_co:
                    coefficient = 1
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
                coefficient = 10 * coefficient + int(v)
                has_co = True
        if coefficient:
            if operator:
                num += coefficient
            else:
                num -= coefficient
        if not num and not x:
            return "Infinite solutions"
        elif not x:
            return "No solution"
        else:
            return 'x=' + str(0 - num // x)