'''
Pro150，升级版
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

  这里加了阶乘，并且要抛出异常
'''
from collections import deque
import math
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = deque()
        i = 0
        ope = ['+','-','*','/']
        while i < len(tokens):
            if tokens[i][-1].isdigit():
                stack.append(float(tokens[i]))
            else:
                # 异常一：没有数字
                if not stack:
                    return 'No number!'
                # 异常2：阶乘是float
                if tokens[i] == '!':
                    try:
                        stack[-1] = math.factorial(stack[-1])
                    except:
                        return 'Only integral for factorial'
                elif tokens[i] in ope:
                    # 异常三：只有一个数字
                    if len(stack) < 2:
                        return 'No enough number'
                    if tokens[i] == '+':
                        stack.append(stack.pop() + stack.pop())
                    elif tokens[i] == '-':
                        stack.append(-stack.pop() + stack.pop())
                    elif tokens[i] == '*':
                        stack.append(stack.pop() * stack.pop())
                    else:
                        n1 = stack.pop()
                        # 异常4：除以0
                        if not n1:
                            return 'Divided by zero'
                        else:
#                             注意python 6/-132 = -1,而这里要的是0
#                             stack.append(int(float(stack.pop())/n1))
                            stack.append(stack.pop() / n1)
                # 异常5：不合理的输入
                else:
                    return 'Invaild operation'
            i+=1
        #     异常6：多余数字
        if len(stack) > 1:
            return 'hava other number'
        return stack[-1]
if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(['-1','0','!','+','0','/']))