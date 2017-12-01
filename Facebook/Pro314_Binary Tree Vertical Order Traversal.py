'''
Facebook_Medium
11.8 12:52pm
'''
# Definition for a binary tree node.

# 方法一 用dict

def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]

# 方法二 自己构造双向链表
from collections import deque
class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        q1 = deque()
        nodeList = NodeList([root.val])
        temp = nodeList
        q1.append((root, nodeList))
        # q2 = deque()
        while (q1):
            (node, node_l) = q1.popleft()
            if node.left:
                if node_l.before:
                    nodeList = node_l.before
                    nodeList.l.append(node.left.val)
                else:
                    nodeList = NodeList([node.left.val])
                    node_l.before = nodeList
                    nodeList.after = node_l
                q1.append((node.left, nodeList))
            if node.right:
                if node_l.after:
                    nodeList = node_l.after
                    nodeList.l.append(node.right.val)
                else:
                    nodeList = NodeList([node.right.val])
                    node_l.after = nodeList
                    nodeList.before = node_l
                q1.append((node.right, nodeList))

        center = temp.after
        while center:
            ans.append(center.l)
            center = center.after
        while temp:
            ans.insert(0, temp.l)
            temp = temp.before
        return ans


class NodeList(object):
    def __init__(self, l):
        self.l = l
        self.before = None
        self.after = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    s.verticalOrder(node1)