# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        node1 = slow
        node2 = node1.next
        node1.next = None
        while node2:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3

        while node1:
            if node1.val != head.val:
                return False
            node1 = node1.next
            head = head.next
        return True