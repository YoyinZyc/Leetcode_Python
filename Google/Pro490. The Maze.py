'''
按照一个方向走，撞到墙才能改方向
要求找到能不能最后停到destination的位置

思路:
BFS
'''
class Solution:
    def hasPath(self, maze, start, destination):
        # 队列
        Q = [start]
        n = len(maze)
        m = len(maze[0])
        # 四个方向
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while Q:
            # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
            i, j = Q.pop(0)
            # 标识走到过
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in dirs:
                row = i + x
                col = j + y
                # 当合理且不是墙，沿这个方向一直走
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                # 不是墙
                if maze[row][col] == 0:
                    Q.append([row, col])

        return False
