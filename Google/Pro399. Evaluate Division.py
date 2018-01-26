'''
题意：
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

思路：
这是一个图论题，要用dfs解决
建一个无向图，用map存储

可变为汇率转换，单位转换之
类的题目
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


'''
union find
都是pre-calculate好啦，读取的时候是O(1)
特点是有union和find两个方法
'''
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # 记录父子关系
        father = dict()
        # 记录值
        value = dict()

        # 找到终点
        def find(point):
            if father[point] != point:
                return find(father[point])
            return point

        def union(p1, p2):
            f1 = find(p1)
            f2 = find(p2)
            if f1 != f2:
                # 这里也可以是father[f1] = f2这个就是表示一个关系
                father[f2] = f1

        for i in range(len(values)):
            eq1 = equations[i][0]
            eq2 = equations[i][1]
            if eq1 not in father and eq2 not in father:
                father[eq1] = eq1
                father[eq2] = eq2
                value[eq1] = values[i]
                value[eq2] = 1.0
            elif eq1 not in father:
                father[eq1] = eq1
                value[eq1] = value[eq2] * values[i]
            elif eq2 not in father:
                father[eq2] = eq2
                value[eq2] = value[eq1] / values[i]

            else:
                # 找到eq1的终点
                top = find(eq1)
                # 对于father中每一个和eq1终点相同的，都是以同一个为参照物
                for v in father:
                    if find(v) == top:
                        # 更新这些value的值，如果现在eq2成为参照物，那么就会更新
                        value[v] = value[v] * values[i] * value[eq2]
            union(eq1, eq2)

        ret = []
        for v in queries:
            # 有其他字符
            if v[0] not in father or v[1] not in father:
                ret.append(-1.0)
                continue
            # 只有有相同终点的才可以算
            if find(v[0]) == find(v[1]):
                ret.append(value[v[0]] / value[v[1]])
            else:
                ret.append(-1.0)
        return ret
'''
BFS
'''
class Solution(object):
    def calcEquation(self, equations, values, queries):

        graph = {}

        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]

            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1 / value)

        def find_path(query):
            b, e = query

            if b not in graph or e not in graph:
                return -1.0

            q = collections.deque([(b, 1.0)])
            visited = set()

            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product * value))

            return -1.0

        build_graph(equations, values)
        return [find_path(q) for q in queries]