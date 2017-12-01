class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        self.helper(nums, [], ans)
        return ans

    def helper(self, nums, path, ans):
        ans.append(path)
        i = 0
        while i < len(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                self.helper(nums[i + 1:], path + [nums[i]], ans)
            i += 1


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res