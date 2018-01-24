# 题意：Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
# Input:3   Output:3
# 思路：先找到阈值
# 0-9：9个    10-100：180个...
# 然后找到n缩在的区间
# 最好带一个例子思考
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 找阈值
        level = [0]
        i = 1
        while level[-1] < 2 ** 31:
            level.append(level[-1] + i * 9 * 10**(i-1))
            i+=1
        i = len(level)-1
        # 找下界
        while i >= 0:
            if level[i]<n:
                break
            i-=1
        # 要把n-1，这样才能计数
        n = n-1
        # 余数
        n1 = (n-level[i]) % (i+1)
        # 注意要加上10 ** i
        n2 = (n-level[i]) // (i+1) + 10**i
        # 返回digit
        return n2 // (10 ** (i-n1)) % 10