'''
题意：
找到二叉树中最大的BST，返回BST中node的个数

思路:
自下向上递归
'''
class TreeNode(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
def largestSubTree(root):
    '''

    :param root: 传入node
    :return:
        第一位是返回子树是不是都是BST
        第二位返回子树最小
        第三位返回子树最大
        第四位返回子树中最大的BST
    '''
    def helper(node):
        if not node:
            return (1,0,0,0)
        left = helper(node.left)
        right = helper(node.right)
        # 如果左右都是BST，且当前node也满足BST
        # 特殊情况是子树中有空，要判断最后一位是不是0，是0也是BST
        if left[0] and right[0] and (left[2] < node.val or not left[3])  and (right[1] > node.val or not right[3]):
            mi = left[1]
            ma = right[2]
            if not left[3]:
                mi = node.val
            if not right[3]:
                ma = node.val
            return (1,mi,ma, left[3]+right[3]+1)
        else:
            return (0,0,0,max(left[3],right[3]))
    return helper(root)
if __name__ == '__main__':
    n1 = TreeNode(50)
    n1.left = TreeNode(10)
    n1.right = TreeNode(60)
    n1.left.left = TreeNode(5)
    n1.left.right = TreeNode(20)
    n1.right.left = TreeNode(55)
    n1.right.left.left = TreeNode(45)
    n1.right.right = TreeNode(70)
    n1.right.right.left = TreeNode(65)
    n1.right.right.right = TreeNode(80)
    print(largestSubTree(n1))