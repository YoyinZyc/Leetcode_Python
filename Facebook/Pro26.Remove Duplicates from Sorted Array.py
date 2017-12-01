class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 1
        new_pointer = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                i+=1
            else:
                nums[new_pointer] = nums[i]
                new_pointer+=1
                count += 1
        return count