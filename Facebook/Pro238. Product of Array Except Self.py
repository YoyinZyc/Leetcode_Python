class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        if len(nums) == 1:
            return [0]
        ans = [1]
        for i in range(0,len(nums)-1):
            ans.append(ans[-1] * nums[i])
        for i in range(len(nums)-1, 0, -1):
            ans[i-1] *= nums[i]
            nums[i-1] *= nums[i]
        return ans