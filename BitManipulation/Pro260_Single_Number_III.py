'''
BitManipulation_Medium
10.10 11:40pm
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        for v in nums:
            if v ^ xor in nums:
                return [v, v ^ xor]
