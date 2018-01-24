'''
判断两个数是否相似
         a                         a
      b       c                c       b
   d    e    f   g         g    f     d  e
时间复杂度：
n^2
因为我们要去看两个孩子，而且对两个孩子来说有两种similar的可能性
（排列一样或者flip了），因此每一层的复杂度是4*（num of nodes）, 一共有logN层，所以复杂度是4^logN = N^2

如果需要把数md5 hash：
可以把input变成list of edges的形式，比如（A (B)(C))可以转化成[（A C）,(A B)]，
如果tree是相似的，这个list of edges内容应该是相同的。
'''
def checkSimilar(root1, root2):
    if not root1 or not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return checkSimilar(root1.left,root2.left) and checkSimilar(root1.right, root2.right) or checkSimilar(root1.left, root2.right) and checkSimilar(root1.right,root2.left)
