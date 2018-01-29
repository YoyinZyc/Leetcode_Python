'''
题意：
找到bt中最长连续的段
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.longest_path = 1
        '''
        link是parent和当前节点的差，用于判断能不能和parent连接
        返回值是要和parent连起来的长度
        '''
        def helper(node, link):
            if not node:
                return 0
            # 左右的返回值
            left = None
            right = None

            if node.left:
                # 这个if-else用于判断传入的link值
                if abs(node.val - node.left.val) == 1:
                    left = helper(node.left, node.val - node.left.val)
                else:
                    left = helper(node.left, 0)
            if node.right:
                if abs(node.val - node.right.val) == 1:
                    right = helper(node.right, node.val - node.right.val)
                else:
                    right = helper(node.right, 0)

            if not left and not right:
                return 1 if link else 0
            elif not left:
                self.longest_path = max(self.longest_path, right + 1)
                if node.val - node.right.val == link:
                    return right + 1
                else:
                    return 1 if link else 0
            elif not right:
                self.longest_path = max(self.longest_path, left + 1)
                if node.val - node.left.val == link:
                    return left + 1
                else:
                    return 1 if link else 0
            else:
                # 左右中可以连起来
                if node.val - node.left.val == node.right.val - node.val:
                    self.longest_path = max(self.longest_path, left + right + 1)
                # 不可以，选长的连起来
                else:
                    self.longest_path = max(self.longest_path, left + 1, right + 1)

                ret = 1 if link else 0
                # 左
                if link == node.val - node.left.val:
                    ret = max(ret, left + 1)
                # 右
                if node.val - node.right.val == link:
                    ret = max(ret, right + 1)
                return ret

        helper(root, 0)
        return self.longest_path



