'''
Facebook_Medium
11.10 11:10am
'''
import random

# 方法一：不需要extra space，时间复杂度是O(n)

class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ret = 0
        count = 0
        for i, v in enumerate(self.nums):
            if v != target:
                continue
            else:
                if random.randrange(0, count + 1) == 0:
                    ret = i
                count += 1
        return ret

# 方法2：需要extra space，时间复杂度是O(1)
class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = dict()
        for i, v in enumerate(nums):
            if v in self.d:
                self.d[v].append(i)
            else:
                self.d[v] = [i]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return self.d[target][random.randrange(0, len(self.d[target]))]