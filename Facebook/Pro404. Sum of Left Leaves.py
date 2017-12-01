# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, False)
    def helper(self, root, isLeft):
        if not root:
            return 0
        if not root.left and not root.right and isLeft:
            return root.val
        return self.helper(root.left,True) + self.helper(root.right,False)