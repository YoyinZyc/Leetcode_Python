'''
Sort_Medium
9.22 8:55pm
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        return self.helper(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, target)

    def helper(self, matrix, min_x, max_x, min_y, max_y, target):
        if min_x > max_x or min_y > max_y:
            return False
        i = min_x
        j = min_y
        while True:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                if i == max_x:
                    return self.helper(matrix, min_x, max_x, j + 1, max_y, target)
                elif j == max_y:
                    return self.helper(matrix, i + 1, max_x, min_y, max_y, target)
                else:
                    i += 1
                    j += 1
            else:
                return self.helper(matrix, min_x, i - 1, j, max_y, target) or self.helper(matrix, i, max_x, min_y,
                                                                                          j - 1, target)

