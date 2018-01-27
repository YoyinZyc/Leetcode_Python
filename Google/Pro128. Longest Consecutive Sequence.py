'''
找连续数字的长度

follow-up：
给一个数组， 找出存在的最长的两倍链的长度
把加法换成乘法
'''
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0
        for x in nums:
            if x-1 not in nums:
                y = x+1
                while y in nums:
                    y+=1
                max_len = max(max_len, y-x)
        return max_len
