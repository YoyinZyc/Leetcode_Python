'''
Google_Medium
10.9 11:28pm
'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return nums.index(max(nums))
        if len(nums) == 1:
            return 0
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, low, high):
        if low == high:
            return low
        middle1 = (low + high) // 2
        middle2 = middle1 + 1
        if nums[middle1] > nums[middle2]:
            return self.helper(nums, low, middle1)
        else:
            return self.helper(nums, middle2, high)
