'''
LinkedIn_Easy
10.12 3:35pm
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if not root.left:
            return -1
        # if root.left.val != root.right.val:
        #     return max(root.left.val, root.right.val)
        else:
            left = root.left.val
            right = root.right.val
            if root.left.val == root.val:
                left = self.findSecondMinimumValue(root.left)
            if root.right.val == root.val:
                right = self.findSecondMinimumValue(root.right)
            if left == -1 and right == -1:
                return -1
            if left == -1:
                return right
            if right == -1:
                return left
            return min(left, right)