class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        return self.helper(nums)

    def helper(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        ans = []
        i = 0
        while i < len(nums):
            ret = []
            if i == 0:
                ret = self.helper(nums[1:])
            elif nums[i] != nums[i - 1]:
                ret = self.helper(nums[:i] + nums[i + 1:])
            for r in ret:
                ans.append([nums[i]] + r)
            i += 1
        return ans