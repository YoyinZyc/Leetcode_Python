class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            self.reverse(nums, 0, len(nums) - 1)
            return
        j = len(nums) - 1

        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        self.reverse(nums, i, len(nums) - 1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
