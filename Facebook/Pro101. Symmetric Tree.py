# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q1 = deque()
        q2 = deque()
        q1.append(root)
        while q1:
            left = q1.popleft()
            if left:
                q2.insert(0, left.right)
                q2.insert(0, left.left)
            if not q1:
                temp = q1
                q1 = q2
                q2 = temp
                continue
            right = q1.pop()
            if right:
                q2.append(right.left)
                q2.append(right.right)
            if (not left and right) or (not right and left):
                return False
            if left and right and left.val != right.val:
                return False
            if not q1:
                temp = q1
                q1 = q2
                q2 = temp
                continue
        return True
