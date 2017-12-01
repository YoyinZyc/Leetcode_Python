class Solution:
    def removeBoxes(self, A):
        N = len(A)
        #         n^3
        memo = [[[0] * N for _ in range(N)] for _ in range(N)]

        #     i和j是坐标，k是从右开始有几个数相同
        def dp(i, j, k):
            if i > j: return 0

            if not memo[i][j][k]:
                # 从右往左看，有几个相同的，j左移，k+1
                while j > i and A[j] == A[j - 1]:
                    j -= 1
                    k += 1
                ans = 0
                #                 开始移左边，如果和右边的值相同，可以把右边的一堆和左边的合在一起，先动中间的
                for m in range(i, j):
                    if A[j] == A[m]:
                        ans = max(ans, dp(m + 1, j - 1, 0) + dp(i, m, k + 1))
                memo[i][j][k] = max(ans, dp(i, j - 1, 0) + (k + 1) ** 2)
            return memo[i][j][k]

        return dp(0, N - 1, 0)
