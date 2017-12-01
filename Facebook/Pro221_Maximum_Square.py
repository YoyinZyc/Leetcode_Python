class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        record = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_edge = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        record[i][j] = 1
                    else:
                        record[i][j] = min(record[i - 1][j], record[i][j - 1], record[i - 1][j - 1]) + 1
                    max_edge = max(record[i][j], max_edge)
        return max_edge ** 2
