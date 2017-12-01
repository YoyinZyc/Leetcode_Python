# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
    def helper(self, node):
        if not node:
            return (node,node)
        left_b, left_e = self.helper(node.left)
        right_b, right_e = self.helper(node.right)
        node.left = None
        if left_b:
            node.right = left_b
            if right_b:
                left_e.right = right_b
                # right_e.right = None
                return (node,right_e)
            else:
                return (node,left_e)
        else:
            if right_b:
                node.right = right_b
                return (node,right_e)
            else:
                return (node, node)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None

        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.prev

        self.prev = root