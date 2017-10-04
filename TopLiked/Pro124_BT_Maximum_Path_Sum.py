'''
TopLiked_Medium
10.2 4:11pm
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    m = -float('inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.m

    def helper(self, node):
        if not node:
            return 0
        maxLeft = self.helper(node.left)
        maxRight = self.helper(node.right)
        self.m = max(self.m, max(maxLeft, 0) + max(maxRight, 0) + node.val)

        return max(max(maxLeft, maxRight) + node.val, 0)
