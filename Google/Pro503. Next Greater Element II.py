'''
题意：
给一个数列，要求找到下一个greater，是circular的
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.

思路：
用stack，倒着来
'''
from collections import deque
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = deque()
        # 返回数组
        ret = [-1 for _ in range(len(nums))]
        # 因为是circular，循环两遍，倒着来
        for i in range(len(nums) * 2-1, -1, -1):
            # 当stack不为空且栈顶比当前数字小的时候。pop
            while stack and stack[-1] <= nums[i%len(nums)]:
                stack.pop()
            # 如果现在栈不为空，当前位置的next greater就是栈顶
            if stack:
                ret[i%len(nums)] = stack[-1]
            # 否则，不变，把当前值append进stack
            stack.append(nums[i%len(nums)])
        return ret