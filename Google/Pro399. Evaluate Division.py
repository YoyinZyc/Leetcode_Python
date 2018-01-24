'''
题意：
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

思路：
这是一个图论题，要用dfs解决
建一个无向图，用map存储

'''
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # 定义record
        record = dict()
        i = 0
        # 建初始图
        while i < len(equations):
            record[equations[i][0]] = record.get(equations[i][0], dict())
            record[equations[i][0]][equations[i][1]] = values[i]
            record[equations[i][1]] = record.get(equations[i][1], dict())
            record[equations[i][1]][equations[i][0]] = 1 / values[i]
            i += 1
        ans = []
        # 计算query
        for v in queries:
            ret = self.dfs(record, record.get(v[0]), v[1], [v[0]])
            if ret:
                ans.append(ret)
                # 缓存结果进入record
                record[v[0]][v[1]] = ret
                record[v[1]][v[0]] = 1 / ret
            else:
                ans.append(-1.0)
        return ans


    def dfs(self, record, d, b, visited):
        '''
        :param record: 图的record
        :param d: 前一个点的后继点集，用一个dict存储
        :param b: 最终的节点
        :param visited: 已经访问过的点
        :return: 返回0说明没找到，其他返回结果
        '''
        if not d:
            return 0
        if b in d:
            return d[b]
        for key in d:
            if key not in visited:
                visited.append(key)
                ret = self.dfs(record, record.get(key), b, visited)
                if ret:
                    return ret * d[key]
        return 0


