'''
BFS_Medium
9.13 1:53pm
'''

from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        d = dict()
        for e in edges:
            d.setdefault(e[0],[]).append(e[1])
            d.setdefault(e[1],[]).append(e[0])

        index = []
        mi = float('inf')
        # print(d)
        for i in range(n):
            q = deque()
            set = []
            q.append(i)

            count = 0
            level1 = 0
            level2 = 1
            while q:
                v = q.popleft()
                set.append(v)
                # if(not all(k in set for k in d[v])):
                if level1 == 0:
                    count+=1
                    level1 = level2
                    level2 = 0
                level1 -= 1
                for k in d[v]:
                    level2+=1
                    q.append(k)
            print (count)
            if count < mi:
                mi = count
                index = []
                index.append(i)
            elif count == mi:
                index.append(i)
        return  index
