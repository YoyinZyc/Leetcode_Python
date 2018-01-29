'''
线段树
Segment Tree
用于解决区间问题

如果要写区间更新的方法，tree里面存储index
left root*2+1
right root*2+2

http://www.cnblogs.com/TenosDoIt/p/3453089.html
'''
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def createTree(l):
    if len(l) == 1:
        return TreeNode(l[0])
    c = (len(l)-1) // 2
    left = createTree(l[:c])
    right = createTree(l[c:])
    if left.val < right.val:
        parent = TreeNode(left.val)
    else:
        parent = TreeNode(right.val)
    return parent

def query(l, start, end):
    root = createTree(l)
    def helper(node, ns, ne):
        # 查询区间和当前节点区间没有交集
        if start > ne or end< ns:
            return float('inf')
        # 当前节点区间包含在查询区间内
        if start <= ns and end >= ne:
            return node.val
        # 分别从左右子树查询，返回两者查询结果的较小值
        center = (ns+ne) // 2
        left = helper(node.left, ns, center-1)
        right = helper(node.right, center, ne)
        return min(left,right)
    helper(root,0,len(l)-1)