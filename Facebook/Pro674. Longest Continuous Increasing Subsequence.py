class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp = 1
        max_len = 1
        i = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                temp += 1
            else:
                max_len = max(max_len, temp)
                temp = 1
            i += 1
        return max(max_len, temp)
