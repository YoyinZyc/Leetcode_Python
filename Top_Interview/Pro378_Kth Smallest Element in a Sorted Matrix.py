'''
Top_Interview_Medium
10:15 3:46pm
'''
from queue import PriorityQueue


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        q = PriorityQueue()
        visited = [[0 for _ in range(n)] for _ in range(n)]

        q.put([0, 0])
        visited[0][0] = 1
        count = 0
        while q:
            v = q.get()
            print(v)
            count += 1

            if count == k:
                return matrix[v[0]][v[1]]
            if v[0] < n - 1 and not visited[v[0] + 1][v[1]]:
                down = matrix[v[0] + 1][v[1]]
            else:
                down = False
            if v[1] < n - 1 and not visited[v[0]][v[1] + 1]:
                right = matrix[v[0]][v[1] + 1]
            else:
                right = False
            print(right)
            print(down)
            if right and down:
                visited[v[0]][v[1] + 1] = 1
                visited[v[0] + 1][v[1]] = 1
                if right < down:
                    q.put([v[0], v[1] + 1])
                    q.put([v[0] + 1, v[1]])
                else:
                    q.put([v[0] + 1, v[1]])
                    q.put([v[0], v[1] + 1])
            elif down:
                visited[v[0] + 1][v[1]] = 1
                q.put([v[0] + 1, v[1]])
            elif right:
                visited[v[0]][v[1] + 1] = 1
                q.put([v[0], v[1] + 1])





if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2],[1,3]]
    k = 2
    s.kthSmallest(matrix, k)