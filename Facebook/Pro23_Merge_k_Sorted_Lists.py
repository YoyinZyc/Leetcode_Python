'''
Facebook_Easy
10.3 11:48pm
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        if len(lists) == 1:
            return lists[0]
        center = len(lists) // 2
        left = self.mergeKLists(lists[:center])
        right = self.mergeKLists(lists[center:])
        return self.merge(left, right)

    def merge(self, node1, node2):
        if not node1 and not node2:
            return node1
        elif not node1:
            return node2
        elif not node2:
            return node1

        head = ListNode(0)
        node = head
        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next

        if node1:
            node.next = node1
        if node2:
            node.next = node2
        return head.next