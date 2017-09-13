'''
Greedy_Medium
9.12 10:46pm
'''


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        if len(nums) == 2 and nums[0] == nums[1]:
            return 1
        # maxL = 0
        count = 2
        j = 1
        while j < len(nums) and nums[j]==nums[j-1]:
            j+=1
        if j == len(nums):
            return 1
        subN = nums[j] - nums[j-1]


        while j < len(nums):


            if (nums[j]-nums[j-1]) * subN > 0:
                subN = subN + nums[j]-nums[j-1]
            elif (nums[j]-nums[j-1]) * subN < 0:
                subN = nums[j]-nums[j-1]
                count+=1
            j+=1

        return count