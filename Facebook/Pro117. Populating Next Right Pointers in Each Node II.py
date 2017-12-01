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
    def connect(self, root):
        level_start = root
        prev = None
        head = None
        while level_start:
            cur = level_start
            while cur:
                if cur.left:
                    if not prev:
                        head = cur.left
                    else:
                        prev.next = cur.left
                    prev = cur.left
                if cur.right:
                    if not prev:
                        head = cur.right
                    else:
                        prev.next = cur.right
                    prev = cur.right
                cur = cur.next
            prev = None
            level_start = head
            head = None