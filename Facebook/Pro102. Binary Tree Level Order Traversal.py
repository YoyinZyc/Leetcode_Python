# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        q1 = deque()
        q2 = deque()
        q1.append(root)

        l = []
        while q1:
            node = q1.popleft()
            if node:
                l.append(node.val)
                q2.append(node.left)
                q2.append(node.right)
            if not q1:
                temp = q2
                q2 = q1
                q1 = temp
                if l:
                    ans.append(l)
                l = []
        return ans

