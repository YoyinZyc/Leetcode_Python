'''
题意：
给了一个数字串和一个k
要求返回每k个一组的滑动窗口的最大值
For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

思路：
用deque双向
O(n)
'''
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        d = deque()
        # 返回值
        out = []
        # 循环
        for i, n in enumerate(nums):
            # 从后向前，对比d中的值和新加入的数字的大小，如果比新加入的小，直接pop出
            while d and nums[d[-1]] < n:
                d.pop()
            # 把新的数字加进去
            d += i,
            # 如果队列首是要最左边的要离开的数，pop出left
            if d[0] == i - k:
                d.popleft()
            # 如果i>=k-1意味已经有了窗口
            if i >= k - 1:
                # 把最左边的数字就是最大的数字加进返回值
                out += nums[d[0]],
        return out