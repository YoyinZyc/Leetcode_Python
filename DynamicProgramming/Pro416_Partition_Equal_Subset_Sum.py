'''
DP_Medium
9.22 5:53am
'''
from collections import deque


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s / 2
        nums.sort(reverse=True)
        if (nums[0] > s):
            return False
        return self.helper(nums, 0, s, len(nums))

    def helper(self, nums, i, target, length):
        if i == length:
            return False
        if target == 0:
            return True
        if target < 0:
            return False
        return self.helper(nums, i + 1, target - nums[i], length) or self.helper(nums, i + 1, target, length)

