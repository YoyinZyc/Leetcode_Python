class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle

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
        return -1
