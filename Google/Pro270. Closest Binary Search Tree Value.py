'''
题意：
找到BST中和target最接近的数字
注意这个target是float类型的

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        sub = float('inf')
        last_val = 0
        while root:
            if root.val < target:
                if target - root.val < sub:
                    last_val = root.val
                    sub = target-root.val
                root = root.right
            elif root.val > target:
                if root.val- target < sub:
                    last_val = root.val
                    sub = root.val-target
                root = root.left
            else:
                return root.val
        return last_val