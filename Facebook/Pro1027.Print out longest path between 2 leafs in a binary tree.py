class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):

    def __init__(self):
        self.max_p = []
        self.max_l = 0
    def diameter(self,root):
        if not root:
            return (0,[])
        left = self.diameter(root.left)
        right = self.diameter(root.right)

        if max(left[0],right[0])+1 > self.max_l:
            self.max_p = left[1] + [root.val] + right[1]
            self.max_l = left[0] + right[0] + 1
        if left[0] > right[0]:
            return (left[0]+1,left[1]+[root.val])
        else:
            return (right[0]+1,right[1]+[root.val])

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node4.left = node8
    node5.left = node6
    node8.left = node7
    s.diameter(node1)
    print (s.max_p)

