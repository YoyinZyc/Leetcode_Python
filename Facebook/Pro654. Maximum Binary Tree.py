'''
Facebook_Medium
11.5 9:58pm
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_v = max(nums)
        max_i = nums.index(max_v)
        node = TreeNode(max_v)
        node.left = self.constructMaximumBinaryTree(nums[:max_i])
        node.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        return node

# 循环
from collections import deque


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        q = deque()
        for v in nums:
            node = TreeNode(v)
            while q and q[-1].val < v:
                node.left = q.pop()
            if q:
                q[-1].right = node
            q.append(node)
        return q[0]

