'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

思路：
Greedy算法，每次比较可以到达的最远距离
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 1
        current = nums[0]
        while i < len(nums):
            # 如果current为0，说明不能到达这个位置，返回False
            if not current:
                return False
            # 比较上一次最远距离-1和当前位置的值
            current = max(current - 1, nums[i])
            i += 1
        return True
