'''
假设你的预算是N，你需要买一块矩形的地皮。给出一个地价的矩阵，问能买到地皮的最大的面积是什么。地价一定是非负数。
比如预算是11.
1 2 3 1
0 1 4 2
1 9 10 4
输出应该是.
1 2 3
0 1 4

关于第二题。其实有点像利口363. 只不过这里保证了元素一定是非负数。
有一个N^3的解法是，枚举上下边界，把矩阵压缩成一行数据。枚举是N^2的，
在一行数据中求出和不大于某个值可以用2 pointer，也就是O(n)。非负数就不需要二分去查找之前的情况
'''
import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # row
        m = len(matrix)
        # col
        n = len(matrix[0]) if m else 0

        M = max(m, n)
        N = min(m, n)
        ans = -float('inf')
        # 遍历行列中短的那一个
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                slist, num = [], 0
                # 加和
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k: ans = max(ans, num)
                    # 二分法查找num-k的位置左边的那一个
                    i = bisect.bisect_left(slist, num - k)
                    if i != len(slist): ans = max(ans, num - slist[i])
                    # 二分插入
                    bisect.insort(slist, num)
        return ans or 0