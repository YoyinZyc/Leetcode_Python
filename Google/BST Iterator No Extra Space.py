'''
BST Iterator
不用额外空间
思路：
每次都重新找
对于每次要返回的点n：
    如果n有right，然后就找到其right的最left为current
    如果没有：找parent
找parent：
    按照value找，要注意如果val比根大，parent不变，因为parent的值小于right

结果:
    end是最右，找parent的时候要对比是不是end了，end就不需要找parent
https://github.com/awangdev/LintCode/blob/master/Java/Binary%20Search%20Tree%20Iterator.java
'''
class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        node = self.root
        while node.left:
            node = node.left
        self.current = root

        node = self.root
        while node.right:
            node = node.right
        self.end = root

    def next(self):
        val = self.current.val
        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
        else:
            self.current = self.findParent(self.current)
        return val

    def findParent(self, node):
        if node == self.end:
            return None

        rt = self.root
        parent = rt
        while rt:
            # 要向右找，直接变成right
            if rt.val < node.val:
                rt = rt.right
            # 向左，改变parent
            elif rt.val > node.val:
                parent = rt
                rt = rt.left
            else:
                return parent