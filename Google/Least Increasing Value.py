'''
一棵树，所有节点的value都是 正整数，问只能增加某些节点 值的情况下，
如何调整使得从 root到所有leaf的path上经过的 节点值之和相等，返回增加的
值的和，使这个和最小

思路：
對於每個節點， 找到左邊子樹和右子樹從leaf 到當前node的值(不算當前 node)，
然後Math.abs(diff (left - right))就是這個節 點需要給左邊或者右邊子樹 增加的值，
後續遍歷到root，就知道總  需要加的值，這裏因爲是正 整數，所以衹有加法沒有減法

中心思想：
尽量往高层的node上面加值
'''
import math
class Solution(object):
    def leastValue(self):
        self.ret = 0
        def helper(root):
            left = helper(root.left)
            right = helper(root.right)
            self.ret += math.abs(left-right)
            return max(left,right)
        return self.ret