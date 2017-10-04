'''
TopLiked_Medium
9.29 2:57pm
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergesort(head)

    def mergesort(self, head):
        if not head:
            return head
        if not head.next:
            return head
        if not head.next.next:
            if head.val > head.next.val:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
            return head
        # separate
        node = head
        middle = head
        while node and node.next:
            node = node.next.next
            middle = middle.next
        start_node_right = middle.next
        middle.next = None
        left = self.mergesort(head)
        right = self.mergesort(start_node_right)
        #         merge
        head = ListNode(0)
        node = head
        while left and right:
            if left.val <= right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        if left:
            node.next = left
        if right:
            node.next = right
        return head.next

