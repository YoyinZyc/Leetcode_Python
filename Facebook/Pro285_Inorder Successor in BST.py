'''
Facebook_Medium
11.8 5:43pm
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # 方法1
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not p:
            return None
        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

    # 方法2
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not p:
            return None
        return self.helper(root, p)[1]

    def helper(self, root, p):

        if not root:
            return (False, None)
        if root == p:
            return (True, self.findNext(root.right))

        ret = self.helper(root.left, p)
        if ret[0]:
            if not ret[1]:
                return (True, root)
            else:
                return ret
        return self.helper(root.right, p)

    def findNext(self, node):
        if not node:
            return None
        ret = self.findNext(node.left)
        if ret:
            return ret
        return node
