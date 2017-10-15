'''
LinkedIn_Medium
10.14 6:27pm
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l_ret = []
        if not root:
            return l_ret
        l_left = self.findLeaves(root.left)
        l_right = self.findLeaves(root.right)
        i = 0
        while i < len(l_left) and i < len(l_right):
            l_ret.append(l_left[i] + l_right[i])
            i+=1
        if i < len(l_right):
            l_ret += l_right[i:]
        if i < len(l_left):
            l_ret += l_left[i:]
        l_ret.append([root.val])
        # print(l_ret)
        return l_ret