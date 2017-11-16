'''
Facebook_Medium
11.8 1:50pm
'''
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = dict()
        max_l = 0
        sum_n = 0
        for i,v in enumerate(nums):
            sum_n += v
            if sum_n == k:
                max_l = i+1
            elif (sum_n-k) in d:
                max_l = max(max_l, i-d[sum_n-k])
            if sum_n not in d:
                d[sum_n] = i
        return max_l