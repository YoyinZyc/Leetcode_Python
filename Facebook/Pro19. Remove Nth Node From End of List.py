# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        while n > 0:
            node1 = node1.next
            n-=1
        if not node1:
            return head.next
        node1 = node1.next
        while node1:
            node2 = node2.next
            node1 = node1.next
        node2.next = node2.next.next
        return head