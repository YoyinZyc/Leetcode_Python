'''
BFS_Medium
9.14 9:38pm
'''

from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        q = deque()
        visited = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for i,row in enumerate(matrix):
            for j,val in enumerate(row):
                if val == 0:
                    visited[i][j] = 1
                    q.append([i,j])
        while q:
            val = q.popleft()
            i = val[0]
            j = val[1]
            if i-1>=0 and not visited[i-1][j]:
                matrix[i-1][j] = matrix[i][j] + 1
                visited[i-1][j] = 1
                q.append([i-1,j])
            if i+1 < len(matrix) and not visited[i+1][j]:
                matrix[i+1][j] = matrix[i][j] + 1
                visited[i+1][j] = 1
                q.append([i+1,j])
            if j-1 >= 0 and not visited[i][j-1]:
                matrix[i][j-1] = matrix[i][j] + 1
                visited[i][j-1] = 1
                q.append([i,j-1])
            if j+1<len(matrix[0]) and not  visited[i][j+1]:
                matrix[i][j+1] = matrix[i][j] +1
                visited[i][j+1] = 1
                q.append([i,j+1])
        return matrix