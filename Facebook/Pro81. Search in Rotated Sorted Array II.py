class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        if target == nums[0]:
            return True
        if target == nums[-1]:
            return True
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return True
            if nums[end] != nums[start]:
                if nums[middle] > target:
                    if nums[middle] > nums[end] and nums[start] > target:
                        start = middle + 1
                    else:
                        end = middle - 1
                else:
                    if nums[middle] < nums[start] and nums[end] < target:
                        end = middle - 1
                    else:
                        start = middle + 1
            else:
                start += 1
        return False
