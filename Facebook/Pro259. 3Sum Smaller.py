'''
Facebook_Medium
11.8 2:59pm
'''
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            t = target - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                while k > j and nums[j] + nums[k] >= t:
                    k -= 1
                count += (k - j)
                j += 1
        return count

