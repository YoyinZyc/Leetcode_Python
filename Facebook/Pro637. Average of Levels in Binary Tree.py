# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        q1 = deque()
        q2 = deque()
        q1.append(root)
        level_sum = 0
        level_count = 0
        while q1:
            node = q1.popleft()
            if node:
                level_sum += node.val
                level_count += 1
                q2.append(node.left)
                q2.append(node.right)
            if not q1:
                if level_count:
                    ans.append(level_sum / level_count)
                    level_count = 0
                    level_sum = 0
                    temp = q1
                    q1 = q2
                    q2 = temp
                else:
                    return ans
        return ans

