'''
Facebook_hard
11.11 6:27pm
'''
# 方法一：
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        record = dict()
        nums = set(nums)
        for v in nums:
            left = record.get(v-1, 0)
            right = record.get(v+1, 0)
            s = left + right + 1
            record[v] = s
            max_len = max(s, max_len)
#             record boundry
            record[v-left] = s
            record[v+right] = s
        return max_len
#  方法二：
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
if __name__ == '__main__':
    s = Solution()
    s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])