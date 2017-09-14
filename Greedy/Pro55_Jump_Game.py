'''
Greedy_Medium
9.13 4:09pm
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                return False

            farthest = 0
            k = 0
            for j in range(1,nums[i]+1):
                if i + j >= len(nums)-1 :
                    return True
                if j + nums[i+j] > farthest:
                    k = j
                    farthest = j + nums[i+j]
            i = i + k
        return True
                