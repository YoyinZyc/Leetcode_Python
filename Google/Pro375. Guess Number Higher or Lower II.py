'''
猜数字，garuntee的钱
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.

思路：
n^3 DP

'''
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # record记录
        record = [[0 for _ in range(n+1)]for _ in range(n+1)]
        # 根据start和end获得钱数
        def getMoney(start, end):
            # 是1，返回start
            if end-start == 1:
                return start
            ret = float('inf')
            # 以start和end之间的每个数为mid，找最小的，在哪里分两半最小
            i = start+1
            while i < end:
                # max左右大的
                ret = min(i+max(record[start][i-1],record[i+1][end]),ret)
                i+=1
            return ret
        # 2d循环构建record
        for i in range(1,n+1):
            # 内层循环反置
            for j in range(i-1,0,-1):
                record[j][i] = getMoney(j,i)
        return record[1][n]