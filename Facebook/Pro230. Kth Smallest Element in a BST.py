# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s = deque()
        while root or s:
            while root:
                s.append(root)
                root = root.left
            if k == 1:
                return s.pop().val
            else:
                root = s.pop().right
                k -= 1
