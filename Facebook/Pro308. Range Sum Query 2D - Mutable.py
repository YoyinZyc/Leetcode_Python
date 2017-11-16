'''
Facebook_Hard
11.08 11:10pm
'''

# 方法1 ：时刻更新
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col - 1]
        self.matrix = matrix

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col - 1]

        diff = original - val

        for y in xrange(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in xrange(row1, row2 + 1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1 - 1]
        return sum

# 方法2
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = 0
        if not (row1 < 0 or row1 >= len(self.matrix) or row2 < 0 or row2 >=len(self.matrix) or col1 <0 or col1 >= len(self.matrix[0]) or col2 < 0 or col2 >= len(self.matrix[0])):
            for i in range(row1,row2):
                ret += sum(self.matrix[i][col1:col2+1])
        return ret

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)