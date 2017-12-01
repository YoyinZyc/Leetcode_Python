class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_p = nums[0]
        m1 = nums[0]
        m2 = nums[0]
        i = 1
        while i < len(nums):
            m1,m2 = min(m1*nums[i],m2*nums[i],nums[i]),max(m2*nums[i],m1*nums[i],nums[i])
            max_p = max(max_p,m2)
            i+=1
        return max_p