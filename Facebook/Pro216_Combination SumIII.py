class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.helper([], k, n, 1, ans)
        return ans

    def helper(self, path, k, n, i, ans):
        if k == 0:
            if n == 0:
                ans.append(path)
            return

        for j in range(i, 10):
            if j > n:
                return
            self.helper(path + [j], k - 1, n - j, j + 1, ans)