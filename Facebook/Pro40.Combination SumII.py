class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        self.helper([], ans, candidates, target)
        return ans

    def helper(self, path, ans, candidates, target):
        if target == 0:
            ans.append(path)
            return
        if target < 0 or not candidates:
            return
        for i, v in enumerate(candidates):
            if i != 0 and v == candidates[i - 1]:
                continue
            if v > target:
                return
            elif v == target:
                # path.append(v)
                ans.append(path + [v])
            else:
                self.helper(path + [v], ans, candidates[i + 1:], target - v)
