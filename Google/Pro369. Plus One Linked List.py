'''
题意：给一个linkedlist 加上1

思路：
1. reverse
    先reverse
    加1
    再reverse
2. 递归
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # reverse
        def reverse(head):
            n1 = head
            n2 = head.next
            n1.next = None
            while n2:
                n3 = n2.next
                n2.next = n1
                n1 = n2
                n2 = n3
            return n1
        # 先reverse
        node = reverse(head)
        # 加1
        n = node
        c = 1
        while n.next:
            n.val = n.val + c
            if n.val == 10:
                n.val = 0
                c = 1
            else:
                c = 0
            n = n.next
        n.val = n.val + c
        if n.val == 10:
            n.val = 0
            c = 1
        else:
            c = 0
        if c == 1:
            new_n = ListNode(1)
            n.next = new_n
        # reverse回来
        return reverse(node)
# 递归
class Solution:
    def helper(self, node):
        # 如果还有下一个，继续递归
        if node.next:
            self.helper(node.next)
        # 否则，最后一个+1
        else:
            node.val += 1
        # 进位
        if node.next and node.next.val >= 10:
            node.next.val = 0
            node.val += 1


    def plusOne(self, head):
        self.helper(head)
        # 如果第一位是10，加一个新的结点
        if head.val >= 10:
            head.val = 0
            result = ListNode(1)
            result.next = head
            return result
        return head