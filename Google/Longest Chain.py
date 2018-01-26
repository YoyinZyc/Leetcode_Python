'''
给出公司并购的关系列表，比 如
["baidu", "ofo"],.
["mobike", "alibaba"],
] 表示baidu并购了ofo，摩拜并购 了阿里巴巴 求最长的一个并购链。保证无 环。

思路：
先找到in和out的dict
然后DFS
'''
def longestChain(l):
    d_in = dict()
    d_out = dict()
    for v in l:
        d_out[v[0]] = d_out.get(v[0],[])
        d_out[v[0]].append(v[1])

        d_in[v[0]] = d_in.get(v[0],[])
        d_in[v[1]] = d_in.get(v[1],[])
        d_in[v[1]].append(v[0])
    max_l = 0
    record = dict()
    def helper(k):
        #如果不在out里，说明没有出度，返回1
        if k not in d_out:
            record[k] = 1
        else:
            # 如果已经计算过，返回record[k]
            if k in record:
                return record[k]
            record[k] = 0
            for v in d_out[k]:
                # 返回最大的
                record[k] = max(record[k], helper(v)+1)
        return record[k]

    for k in d_in:
        # 对于所有入度为0的点
        if not d_in[k]:
            max_l = max(max_l,helper(k))
    return max_l
if __name__ == '__main__':
    l = [['a','b'],['a','v'],['b','v'],['b','c'],['v','f']]
    print(longestChain(l))