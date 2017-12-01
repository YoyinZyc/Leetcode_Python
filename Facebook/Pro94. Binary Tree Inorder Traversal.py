# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = deque()
        ret = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            ret.append(node.val)
            root = node.right
        return ret
