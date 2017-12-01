# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 如果k=1，直接返回head
        if k <= 1:
            return head
        # 设置一个dummy head在原本的head之前
        psydu = ListNode(0)
        psydu.next = head
        # n1是上一次reverse返回的尾节点，连接着下一次reverse开始的点
        n1 = psydu
        n2 = head

        count = 0
        while n2:
            n2 = n2.next
            count += 1
            # 当count=k的时候已经获得了k个可以reverse的点
            if count == k:
                # 把这k个点reverse
                ret = self.reverse(n1.next, k)
                # 返回值的第一个是reverse后新的head
                n1.next = ret[0]
                # 返回值的第二个是下一次reverse开始的点
                n2 = ret[1]
                # 返回值的第三个是这次reverse的尾节点
                n1 = ret[2]
                count = 0
        return psydu.next

    def reverse(self, node, count):
        # 这个begin记录了当前的开头，也就是reverse结束后的结尾
        begin = node

        n1 = node
        n2 = node.next
        while count > 1:
            count -= 1
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        # 这个n2就是下一次reverse的开头，先和begin连起来
        begin.next = n2
        return (n1, n2, begin)
