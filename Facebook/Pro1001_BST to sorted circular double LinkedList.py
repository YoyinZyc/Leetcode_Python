class TreeNode(object):
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None

def merge(left,right):
    if not left:
        return right
    if not right:
        return left
    # 两个nodelist的最右边
    right_last = right.left
    left_last = left.left
    # left的最右边的right是right
    left_last.right = right
    # right最右边的right是left
    right_last.right = left
    # right的最左边是left的最右边
    right.left = left_last
    # left的左边是right的最右边
    left.left = right_last

    return left
def bTreeToCList(root):
    if not root:
        return root
    left = bTreeToCList(root.left)
    right = bTreeToCList(root.right)

    root.left = root
    root.right = root
    return merge(merge(left,root),right)

