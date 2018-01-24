'''
题意：给了一个0，1的2d matrix要求找到其中行，列或者对角线连续为1的最长的值

思路：
算左上
'''
class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        longl = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                # 初始值
                m = [0,0,0,0]
                if M[i][j] == 1:
                    # 1的初始值就是四个1
                    m = [1,1,1,1]
                    # 行
                    if i > 0:
                        m[0] += M[i-1][j][0]
                    # 列
                    if j>0:
                        m[1] += M[i][j-1][1]
                    # 对角
                    if i>0 and j>0:
                        m[2] += M[i-1][j-1][2]
                    # 反对角
                    if i>0 and j<len(M[0])-1:
                        m[3] += M[i-1][j+1][3]
                    # 保留当前的最大值
                    longl = max(longl,max(m))
                # 更新M[i][j]
                M[i][j] = m
        return longl