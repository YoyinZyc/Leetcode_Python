class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return [self.helper(nums, i, m, True, target), self.helper(nums, m, j, False, target)]
            elif nums[m] > target:
                j = m - 1
            else:
                i = m + 1
        return [-1, -1]

    def helper(self, nums, start, end, left, target):

        if left:
            i = start
            j = end
            while i <= j:
                middle = (i + j) // 2
                if nums[middle] == target:
                    j = middle-1
                else:
                    i = middle+1
            return i
        else:
            i = start
            j = end
            while i <= j:
                middle = (i + j) // 2
                if nums[middle] == target:
                    i = middle+1
                else:
                    j = middle - 1
            return j