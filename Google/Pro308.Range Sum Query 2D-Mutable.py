'''
Facebook_Hard
11.08 11:10pm
'''

# 方法1 ：时刻更新,用于sum比较多
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in range(1, len(row)):
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

        for y in range(col, len(self.matrix[0])):
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
        for x in range(row1, row2 + 1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1 - 1]
        return sum

# 方法2
# 用于update比较多
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
'''
Binary indexed tree 的做法
http://blog.csdn.net/qq508618087/article/details/51303552
        8
        /\
       4 
      /\  
     2  6
    /\  /\
   1 3 5  7
初始化的时候时间复杂度是n log n, 以后每次查询和更新log n logm,
最快
'''
class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        self.tree = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = i + 1
                while m < len(matrix) + 1:
                    n = j + 1
                    while n < len(matrix[0]) + 1:
                        self.tree[m][n] += matrix[i][j]
                        n += n & -n
                    m += m & -m
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        m = row + 1
        while m < len(self.matrix) + 1:
            n = col + 1
            while n < len(self.matrix[0]) + 1:
                self.tree[m][n] += diff
                n += n & -n
            m += m & -m

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        def helper(r, c):
            ret = 0
            m = r + 1
            while m > 0:
                n = c + 1
                while n > 0:
                    ret += self.tree[m][n]
                    n -= n & -n
                m -= m & -m

            return ret

        return helper(row2, col2) + helper(row1 - 1, col1 - 1) - helper(row1 - 1, col2) - helper(row2, col1 - 1)