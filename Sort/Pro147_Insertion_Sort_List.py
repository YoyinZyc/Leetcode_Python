'''
Sort_Medium
9.19 6:31pm
'''




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        end = head
        while end.next:
            if end.next.val < head.val:
                node = end.next
                end.next = end.next.next
                node.next = head
                head = node
            elif end.next.val >= end.val:
                end = end.next
            else:
                indexNode = head
                while indexNode.next:
                    if end.next.val >= indexNode.val and end.next.val < indexNode.next.val:
                        node = end.next
                        end.next = end.next.next
                        node.next = indexNode.next
                        indexNode.next = node
                        break
                    indexNode = indexNode.next
        return head



