class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i= 0
        while i < len(nums):
            cur = nums[i]
            # 不断交换cur和nums[cur-1]; 跳出条件是cur不在1-len(nums)中间或者nums[cur-1]已经是cur
            while cur <= len(nums) and cur >= 1 and nums[cur-1] != cur:
                nums[cur-1],cur = cur,nums[cur-1]
            i+=1
        i = 1
        # 再遍历一遍，直到nums[i-1] != i
        while i <= len(nums) and nums[i-1] == i:
            i+=1
        return i