'''
Uber_Medium
10.29 7:28pm
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        node_map = dict()
        new_node = UndirectedGraphNode(node.label)
        node_map[node] = new_node

        q = deque()
        for v in node.neighbors:
            q.append(v)
        q.append('#')
        q2 = deque()
        n2 = new_node
        while q:
            n = q.popleft()
            print(n)
            if n == '#':
                if q2:
                    n2 = q2.popleft()
                else:
                    break
            else:
                if n in node_map:
                    new_n = node_map[n]
                    n2.neighbors.append(new_n)
                else:
                    new_n = UndirectedGraphNode(n.label)
                    node_map[n] = new_n
                    for v in n.neighbors:
                        q.append(v)
                    q.append('#')

                    n2.neighbors.append(new_n)
                    q2.append(new_n)
        return new_node