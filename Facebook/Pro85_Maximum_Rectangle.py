
'''
Facebook_Hard
10.7 3:44pm
'''
from collections import deque

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 如果matrix为空，返回0
        if not matrix:
            return 0
        maximum = 0
        # 用一个int类型的count数组来存储
        count = [0 for _ in range(len(matrix[0]))]
        for row in matrix:
            # 把当前行的每一个数字加进count
            for i, v in enumerate(row):
                if v == '1':
                    count[i] += 1
                else:
                    count[i] = 0
            # print(count)
            stack = deque()
            stack.append(-1)
            for i, num in enumerate(count):
                # 当当前值小于栈顶的时候，一直pop
                while stack[-1] != -1 and num < count[stack[-1]]:
                    right = stack.pop()
                    # 算面积
                    maximum = max(maximum, count[right] * (i - stack[-1] - 1))
                # 当当前值比栈顶大的时候或者stack栈顶为-1一直append
                stack.append(i)
            # 直到stack栈顶为-1，一直pop
            while stack[-1] != -1:
                maximum = max(maximum, count[stack.pop()] * (len(count) - stack[-1] - 1))
                # print(maximum)
        return maximum