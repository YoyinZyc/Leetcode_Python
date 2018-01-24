'''
题意：
有一个matrix，要求找到一条递增的最长的路径
Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

思路：
dfs+dp
'''
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        longest = 0
        # record记录
        record = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # compare
        def compare(i, j, v):
            # 越界 False
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return False
            # 返回是否>
            return matrix[i][j] > v

        def helper(i, j):
            # 越界 0
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return 0
            # 如果已经访问过 返回值
            if record[i][j]:
                return record[i][j]
            v = matrix[i][j]
            # 先置为1
            record[i][j] = 1
            # 上下左右四个方向
            if compare(i - 1, j, v):
                record[i][j] = max(helper(i - 1, j) + 1, record[i][j])
            if compare(i + 1, j, v):
                record[i][j] = max(helper(i + 1, j) + 1, record[i][j])
            if compare(i, j - 1, v):
                record[i][j] = max(helper(i, j - 1) + 1, record[i][j])
            if compare(i, j + 1, v):
                record[i][j] = max(helper(i, j + 1) + 1, record[i][j])
            return record[i][j]
        # 循环
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                record[i][j] = helper(i, j)
                longest = max(longest, record[i][j])
        return longest