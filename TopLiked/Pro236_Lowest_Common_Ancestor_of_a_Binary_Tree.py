'''
TopLiked_Medium
9.28 1:37pm
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        return self.helper(root, p, q)[1]

    def helper(self, root, p, q):
        if not root:
            return [0]
        l1 = self.helper(root.left, p, q)
        l2 = self.helper(root.right, p, q)
        if root == p or root == q:
            print(l1)
            print(l2)
            if l1[0] == 1 or l2[0] == 1:
                return [2, root]
            else:
                return [1]
        else:
            if l1[0] == 2:
                return l1
            elif l2[0] == 2:
                return l2
            elif l1[0] == 1 and l2[0] == 1:
                return [2, root]
            elif l1[0] == 1 or l2[0] == 1:
                return [1]
            else:
                return [0]



