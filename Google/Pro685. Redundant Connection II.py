'''
有向图
除了不能成环外，还不能一个node有两个parent；
如果同时遇见，这两个条件一定发生在同一个node上，只要删除一个就好了
比如：
先遇见两个parent，必然删除一条parent，先删后面那条，如果后面还遇见成环，说明删错了，删除前面那条

如果题目给的就是二叉树或者BST，那么就不需要union find了，检查是否成环或者有两个parent就好
'''
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 因为最多有1000条边，所以最多有2000个node，因为node是从1开始的，所以这边到2001
        parent = [i for i in range(2001)]
        # 记录node的直接parent
        d_parent = [0 for i in range(2001)]

        def find(n):
            # 如果n=parent[n],说明这个点还没有和其他点有链接
            if n == parent[n]:
                return n
            # 否则继续找
            return find(parent[n])
        ret = -1
        for v in edges:
            # v[1]已经有过直接的parent了
            if d_parent[v[1]] != 0:
                # 如果之前已经有过成环的情况
                if ret != -1:
                    # 返回该v[1]之前的parent 和v[1]组成的对
                    return [d_parent[v[1]],v[1]]
                # 否则更新ret
                ret = v
                continue
            # 找到node1的parent
            p1 = find(v[0])
            # 找到node2的parent
            p2 = find(v[1])
            # 如果两个的parent相同，成环
            if p1 == p2:
                # 如果之前已经有过有两个parent的情况
                if ret != -1:
                    # 返回ret[1]之前的parent 和ret[1]组成的对
                    return [d_parent[ret[1]],ret[1]]
                # 否则更新ret
                ret = v
            else:
            # 否则把node1的parent的parent设置为node2的parent
                parent[p1] = p2
                d_parent[v[1]] = v[0]
        return ret
