class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        col_record = [0 for _ in range(len(grid[0]))]
        row = 0
        max_b = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    continue
                if j == 0 or grid[i][j-1] == 'W':
                    k = j
                    row = 0
                    while k < len(grid[0]) and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row+=1
                        k+=1
                if i == 0 or grid[i-1][j] == 'W':
                    k = i
                    col_record[j] = 0
                    while k < len(grid) and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_record[j] += 1
                        k+=1
                if grid[i][j] == '0':
                    max_b = max(max_b, col_record[j] + row)
        return max_b