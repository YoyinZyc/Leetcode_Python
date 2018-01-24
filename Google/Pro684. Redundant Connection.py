'''
题意：
有一堆edge，构成一个无向图，删除其中一条边就可以构成一棵树，要求返回这条边
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3

思路：
1.  Union find
2.  DFS
'''


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 因为最多有1000条边，所以最多有2000个node，因为node是从1开始的，所以这边到2001
        parent = [i for i in range(2001)]

        def find(n):
            # 如果n=parent[n],说明这个点还没有和其他点有链接
            if n == parent[n]:
                return n
            # 否则继续找
            return find(parent[n])

        for v in edges:
            # 找到node1的parent
            p1 = find(v[0])
            # 找到node2的parent
            p2 = find(v[1])
            # 如果两个的parent相同，成环
            if p1 == p2:
                return v
            # 否则把node1的parent的parent设置为node2的parent
            parent[p1] = p2


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        record = {}
        # DFS检查有没有成环
        def check_circle(path, n1, n2):
            if n1 == n2:
                return False
            for v in record[n1]:
                if v not in path:
                    if not check_circle(path + [v], v, n2):
                        return False
            return True

        for v in edges:
            if v[0] not in record or v[1] not in record:
                record[v[0]] = record.get(v[0], [])
                record[v[0]].append(v[1])
                record[v[1]] = record.get(v[1], [])
                record[v[1]].append(v[0])
            else:
                if check_circle([], v[0], v[1]):
                    record[v[0]].append(v[1])
                    record[v[1]].append(v[0])
                else:
                    return v

