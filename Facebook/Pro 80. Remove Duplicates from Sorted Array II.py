class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)<2:
            return len(nums)
        i = 2
        j = 2
        while i < len(nums):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j