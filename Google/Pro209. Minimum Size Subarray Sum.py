'''
找到最短连续的一段subarray，和>=s

follow-up：
有负数

'''
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        sum_n = 0
        count = float('inf')
        while i < len(nums):
            sum_n += nums[i]
            if sum_n >= s:
                while j <= i and sum_n >= s:
                    sum_n -= nums[j]
                    j+=1
                count = min(count, i-j+2)
            i+=1
        if count == float('inf'):
            return 0
        return count