'''
题意：
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

思路：
1.  先sort，然后两个两个一组交换
2.  one pass，如果当前是偶数位且当前的数字比前一个小，交换当前位置与前一个
            如果当前是奇数位且当前的数字比前一个大，交换当前位置与前一个
'''
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            # 利用异或
            if i % 2 ^ (nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
