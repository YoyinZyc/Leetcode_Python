# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# from collections import deque
# class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        record = []
        return self.helper(root, k, record)

    def helper(self, root, k, record):
        if root:
            if k - root.val in record:
                return True
            record.append(root.val)
            return self.helper(root.left, k, record) or self.helper(root.right, k, record)
        return False

from collections import deque


class Solution:
    def findTarget(self, root, k):
        iter1 = BTIterator(root, True)
        iter2 = BTIterator(root, False)
        n1 = 0
        n2 = 0
        n1 = iter1.next()
        n2 = iter2.next()
        while n1!=None and n2!=None:
            if n1 == n2:
                return False
            if n1 + n2 == k:
                return True
            elif n1 + n2 < k:
                n1 = iter1.next()
            else:
                n2 = iter2.next()

        return False


class BTIterator(object):
    def __init__(self, root, isLeft):
        self.root = root
        self.stack = deque()
        self.isLeft = isLeft

    def hasNext(self):
        return self.root or self.stack

    def next(self):
        while self.root or self.stack:
            if self.root:
                self.stack.append(self.root)
                if self.isLeft:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
            else:
                node = self.stack.pop()
                if self.isLeft:
                    self.root = node.right
                else:
                    self.root = node.left
                return node.val
        return None

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(0)
    node2 = TreeNode(-1)
    node3 = TreeNode(-3)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node1.left = node2
    node2.left = node3
    node4.right = node5
    node1.right = node4
    s.findTarget(node1, -4)
