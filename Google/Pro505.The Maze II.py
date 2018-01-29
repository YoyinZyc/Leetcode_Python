'''
接上题，这回要求算一共要走过多少个格子

思路：
和1几乎一样，Queue换成PQ
要用priorityqueue，按照路径最短的排序

Time complexity : O(m*n*max(m,n))O(m∗n∗max(m,n)).
Time complexity : O(m*n*\text{max}(m,n))O(m∗n∗max(m,n)).
Complete traversal of maze will be done in the worst case.
Here, mm and nn refers to the number of rows and columns of the maze.
Further, for every current node chosen, we can travel upto a maximum depth
of \text{max}(m,n)max(m,n) in any direction.

Space complexity : O(mn)O(mn). queuequeue size can grow upto m*nm∗n in the worst case.


'''
from queue import PriorityQueue
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        n = len(maze)
        m = len(maze[0])
        direction = [[1,0],[-1,0],[0,-1],[0,1]]
        Q = PriorityQueue()
        Q.put([0,start])
        while not Q.empty():
            # 把路径最小的get出来
            path,posi = Q.get()
            maze[posi[0]][posi[1]] = 2
            if posi == destination:
                return path
            for x,y in direction:
                row = x+posi[0]
                col = y+posi[1]
                # 用一个count记录在这个方向上走了多少
                count = 0
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                    count += 1
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.put([path+count,[row, col]])

        return -1


if __name__ == '__main__':
    s = Solution()
    s.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
[0,4],
[4,4])