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