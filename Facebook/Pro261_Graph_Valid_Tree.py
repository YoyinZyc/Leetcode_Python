from collections import deque
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 1:
            return True
        d = dict()
        count = 0
        for e in edges:
            if e[0] not in d:
                d[e[0]] = []
                count += 1
            d[e[0]].append(e[1])
            if e[1] not in d:
                d[e[1]] = []
                count += 1
            d[e[1]].append(e[0])
        if count != n:
            return False
        visited = [0]
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            count -=1
            for v in d[node]:
                if v in visited:
                    return False
                d[v].remove(node)
                visited.append(v)
                q.append(v)
        return count == 0


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        record = [-1 for _ in range(n)]
        for e in edges:
            x = self.find_root(e[0],record)
            y = self.find_root(e[1],record)
            if x == y:
                return False
            record[y] = x
        return n-1 == len(edges)
    def find_root(self, node,record):
        if record[node] == -1:
            return node
        return self.find_root(record[node], record)