class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid+1
        return nums[high]