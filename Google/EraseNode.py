'''
有一个shouldBeErased用于检查能不能erase这个node
要求返回erase之后剩下的所有树的root
'''
def shouldBeErased(node):
    return True
def EraseNode(root):
    def helper(node, hasParent):
        ret = []
        if shouldBeErased(root):
            ret += helper(root.left, False)
            ret += helper(root.right, False)
        else:
            if not hasParent:
                ret.append(node)
            ret += helper(root.left, True)
            ret += helper(root.right, True)
        return ret