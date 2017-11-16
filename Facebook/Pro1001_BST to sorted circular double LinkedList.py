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
    right_last = right.left
    left_last = left.right

    left_last.right = right
    right_last.right = left
    right.left = left_last
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

