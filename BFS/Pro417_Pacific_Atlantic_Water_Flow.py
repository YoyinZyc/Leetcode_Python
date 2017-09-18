'''
BFS_Medium
9.17 5:16pm
'''

from collections import deque
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        qPacific = deque()
        qAtlantic = deque()
        visitedPacific = [[0 for j in range(n)] for i in range(m)]
        visitedAtlantic = [[0 for j in range(n)] for i in range(m)]
        record = [[[0,0] for j in range(n)]for i in range(m)]
        for i, row in enumerate(record):
            for j, val in enumerate(row):
                if i==0 or j==0:
                    val[0] = 1
                    qPacific.append([i,j])
                    visitedPacific[i][j] = 1
                if i == m-1 or j == n-1:
                    val[1] = 1
                    qAtlantic.appendleft([i,j])
                    visitedAtlantic[i][j] = 1

        neighbor = [[-1,0],[1,0],[0,-1],[0,1]]
        # print(record)
        while qPacific:
            p = qPacific.popleft()

            for v in neighbor:
                if p[0]+v[0]>=0 and p[0]+v[0] <m and p[1]+v[1] >=0 and p[1]+v[1]<n and matrix[p[0] + v[0]][p[1] + v[1]] >= matrix[p[0]][p[1]] and not visitedPacific[p[0]+v[0]][p[1]+v[1]]:
                    record[p[0]+v[0]][p[1]+v[1]][0] = 1
                    visitedPacific[p[0] + v[0]][p[1] + v[1]] = 1
                    qPacific.append([p[0]+v[0], p[1]+v[1]])
        while qAtlantic:
            a = qAtlantic.popleft()
            for v in neighbor:
                if a[0]+v[0]>=0 and a[0]+v[0] <m and a[1]+v[1] >=0 and a[1]+v[1]<n and matrix[a[0] + v[0]][a[1] + v[1]] >= matrix[a[0]][a[1]] and not visitedAtlantic[a[0]+v[0]][a[1]+v[1]]:
                    record[a[0]+v[0]][a[1]+v[1]][1] = 1
                    visitedAtlantic[a[0] + v[0]][a[1] + v[1]] = 1
                    qAtlantic.append([a[0]+v[0], a[1]+v[1]])
        # print(record)
        ret = [[i,j] for j in range(n) for i in range(m) if record[i][j] == [1,1] ]
        return  ret



if __name__ == '__main__':
    s = Solution()
    matrix = [[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]]
    s.pacificAtlantic(matrix)