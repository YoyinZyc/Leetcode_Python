class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        ans = []
        record = []
        for i, v in enumerate(nums):
            if v not in record:
                record.append(v)
                ret = self.permuteUnique(nums[:i] + nums[i + 1:])
                for r in ret:
                    r.insert(0, v)
                    ans.append(r)
        return ans
        # def helper(self, nums):

