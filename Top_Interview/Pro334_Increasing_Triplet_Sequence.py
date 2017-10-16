'''
Top_Interview_Medium
10:15 4:25pm
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        tail1 = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] < tail1:
                tail1 = nums[i]
            elif nums[i] > tail1:
                tail2 = nums[i]
                break
            i+=1
        while i < len(nums):
            if nums[i] < tail1:
                tail1 = nums[i]
            elif nums[i] > tail1 and nums[i] < tail2:
                tail2 = nums[i]
            elif nums[i] > tail2:
                return True
            i+=1
        return False