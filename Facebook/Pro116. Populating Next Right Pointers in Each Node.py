# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
#     递归
    def connect(self, root):
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
#     循环
    def connect(self, root):
        level_start = root
        while level_start:
            cur = level_start
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                cur = cur.next
            level_start = level_start.left