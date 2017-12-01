class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        # 标志是不是往上走
        up = True
        # 坐标
        i = 0
        j = 0
        while True:
            # 如果是往上走的
            if up:
                # i-=1；j+=1
                while i >= 0 and j <= n - 1:
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1
                up = False
                # 因为最后一个会超出边界，所以要把i+=1；j-=1
                i += 1
                j -= 1
                # 如果当前i,j对应的是右下角，则返回re
                if i + 1 == m and j + 1 == n:
                    # print(res)
                    return res
                # 如果到达右边，则下一个开始的点在该点下方
                if j + 1 == n:
                    i = i + 1
                # 如果没有到达右边，则下一个开始的点在该点右侧
                else:
                    j = j + 1
            else:
                # i+=1；j-=1
                while i <= m - 1 and j >= 0:
                    res.append(matrix[i][j])
                    i += 1
                    j -= 1
                up = True
                # i，j返回当前点
                i -= 1
                j += 1
                # 右下角
                if j == n - 1 and i == m - 1:
                    return res
                # 如果到达下边界，则下一个点在右边
                if i + 1 == m:
                    j += 1
                # 否则在下边
                else:
                    i += 1





