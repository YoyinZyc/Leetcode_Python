class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        temp_sum = 0
        min_len = float('inf')
        while i < len(nums):
            temp_sum += nums[i]
            while temp_sum >= s:
                min_len = min(min_len, i - j + 1)
                temp_sum -= nums[j]
                j += 1
            i += 1
        return min_len if min_len < float('inf') else 0
