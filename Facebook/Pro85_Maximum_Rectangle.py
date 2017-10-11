
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

        if not matrix:
            return 0
        maximum = 0
        count = [0 for _ in range(len(matrix[0]))]
        for row in matrix:
            for i, v in enumerate(row):
                if v == '1':
                    count[i] += 1
                else:
                    count[i] = 0
            # print(count)
            stack = deque()
            stack.append(-1)
            for i, num in enumerate(count):
                while stack[-1] != -1 and num < count[stack[-1]]:
                    right = stack.pop()
                    maximum = max(maximum, count[right] * (i - stack[-1] - 1))
                stack.append(i)
            while stack[-1] != -1:
                maximum = max(maximum, count[stack.pop()] * (len(count) - stack[-1] - 1))
                # print(maximum)
        return maximum