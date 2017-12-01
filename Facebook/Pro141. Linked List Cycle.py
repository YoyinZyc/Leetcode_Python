# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n1 = head
        n2 = head
        while n2 and n2.next:
            n1 = n1.next
            n2 = n2.next.next
            if n2 == n1:
                return True
        return False
