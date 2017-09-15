'''
BFS_Medium
9.13 11:08pm
'''

from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        q = deque()   #队列

        d = dict()  #邻接表 出
        d2 = dict()  # 入度
        prerequisites.sort()
        ret = []

        j = 0
        i = 0

        for i in range(numCourses):
            count = 0
            while j < len(prerequisites) and prerequisites[j][0] == i:

                d.setdefault(prerequisites[j][1],[]).append(prerequisites[j][0])
                # print(d)
                d2[prerequisites[j][0]] = d2.get(prerequisites[j][0],0) + 1
                # print(d2)
                count+=1
                j += 1
            if count == 0:
                q.append(i)

        # print(q)
        while q:
            v = q.popleft()
            # print (v)

            if v in d:
                for i in d[v]:
                    d2[i] -= 1
                for k,va in d2.items():
                    if va == 0:
                        q.append(k)
                        d2.pop(k)
            # print(v)
            ret.append(v)

        if any(d2):
            return []
        return ret


