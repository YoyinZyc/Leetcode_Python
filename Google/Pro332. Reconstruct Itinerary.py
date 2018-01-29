'''
给了一堆机票，【from，to】，要求找到一个合理的路线，起点都是JFK
如果有多个合理的路线，则找字典序最小的

思路：
先转换为map
然后dfs
'''
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = {}
        for v in tickets:
            d[v[0]] = d.get(v[0], [])
            d[v[0]].append(v[1])

        for k in d:
            d[k].sort()

        def helper(path, record, count):
            if not count:
                return path
            if path[-1] not in record:
                return []
            for i in range(len(record[path[-1]])):
                v = record[path[-1]].pop(i)
                p = helper(path + [v], record, count - 1)
                if p:
                    return p
                record[path[-1]].insert(i, v)
            return []

        return helper(['JFK'], d, len(tickets))
import collections
def findItinerary(self, tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
    return route[::-1]
