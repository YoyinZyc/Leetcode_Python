from collections import deque
class Solution:
    def diameters(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ds = []
        visited = [[0 for _ in range(len(grid[0]))]for _ in range(len(grid))]
        # 判断这个neighbor是不是没有visit且为1
        def neighbor(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return False
            if grid[i][j]:
                if not visited[i][j]:
                    stack.append((i,j))
                    visited[i][j] = 1
                return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]:
                    stack = deque()
                    stack.append((i,j))
                    visited[i][j] = 1
                    diameter = 0
                    while stack:
                        x,y = stack.pop()
                        if not neighbor(x-1,y):
                            diameter+=1
                        if not neighbor(x+1,y):
                            diameter+=1
                        if not neighbor(x,y+1):
                            diameter+=1
                        if not neighbor(x,y-1):
                            diameter+=1
                    ds.append(diameter)
        return ds
if __name__ == '__main__':
    s = Solution()
    ret = s.diameters([[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,1,0,0],
 [0,0,0,1,1]])
    print(ret)