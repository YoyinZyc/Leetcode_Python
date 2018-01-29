'''
用PriorityQueue+BFS
有一个visit数组
n^2logn
'''
from queue import PriorityQueue


class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        pq = PriorityQueue()
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            pq.put([heightMap[0][i], [0, i]])
            pq.put([heightMap[m - 1][i], [m - 1, i]])
            visited[0][i] = 1
            visited[m - 1][i] = 1
        for i in range(1, m - 1):
            pq.put([heightMap[i][0], [i, 0]])
            pq.put([heightMap[i][n - 1], [i, n - 1]])
            visited[i][0] = 1
            visited[i][n - 1] = 1

        ret = 0

        def checkValid(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y]:
                return False
            return True

        posi = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while not pq.empty():
            h, [x, y] = pq.get()
            for v in posi:
                if checkValid(x + v[0], y + v[1]):
                    if heightMap[x + v[0]][y + v[1]] < h:
                        ret += h - heightMap[x + v[0]][y + v[1]]
                    visited[x + v[0]][y + v[1]] = 1
                    # 注意这里put的height是本身h和h的最大值
                    pq.put([max(heightMap[x + v[0]][y + v[1]], h), [x + v[0], y + v[1]]])
        return ret

