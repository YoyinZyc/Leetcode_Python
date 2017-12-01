import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        return nums[self.quickSelect(nums, len(nums) - k + 1, 0, len(nums) - 1)]

    def quickSelect(self, nums, k, lo, hi):
        i = lo
        j = hi
        pivot = nums[hi]
        while i < j:
            if nums[i] > pivot:
                j -= 1
                self.swap(nums, i, j)
            else:
                i += 1
        self.swap(nums, i, hi)

        m = i - lo + 1
        if m == k:
            return i
        elif m > k:
            return self.quickSelect(nums, k, lo, i - 1)
        else:
            return self.quickSelect(nums, k - m, i + 1, hi)

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
if __name__ == '__main__':
    s = Solution()
    s.findKthLargest([3,4,2,7,8,1,9],3)