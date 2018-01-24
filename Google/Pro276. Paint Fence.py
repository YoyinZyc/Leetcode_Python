'''
有k种颜色和n个木桩，要求不能有超过2个相邻的木桩颜色相同，求一共有多少种方法

dp问题
状态转移方程：
has_same, no_same = no_same, has_same * (k - 1) + no_same * (k - 1)
'''
class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return k
        has_same = 0
        no_same = k
        i = 1
        while i < n:
            has_same, no_same = no_same, has_same * (k - 1) + no_same * (k - 1)
            i += 1
        return has_same + no_same

