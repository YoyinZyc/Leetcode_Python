'''
要求找到BT中连续数字最长的一段，parent要比child小
For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

思路：
递归
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 当前的node，到其parent为止的length，parent的value
        def helper(node, length, value):
            if not node:
                return length
            # 如果当前的node的值比其parent大一，则向下一层传递的length要+1
            if node.val - value == 1:
                return max(helper(node.left, length+1, node.val), helper(node.right, length+1, node.val))
            # 否则length是1，且要和传入的length比较
            else:
                return max(length, helper(node.left, 1, node.val), helper(node.right, 1, node.val))
        if not root:
            return 0
        return helper(root, 1, root.val)