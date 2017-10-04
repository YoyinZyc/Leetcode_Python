'''
TopLiked_Medium
9.28 11:20pm
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_min = [0 for i in range(len(nums))]
        l_min[0] = nums[0]
        for i in range(1, len(nums)):
            s = [l_min[i - 1] * nums[i], nums[i - 1] * nums[i], nums[i]]
            s.sort()
            l_min[i] = s[0]
            nums[i] = s[2]
        return max(nums)
