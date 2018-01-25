'''
[['a', 'N', 'b'], ['b', 'N', 'c'], ['c', 'S', 'a']] 类似这样的input。
['a', 'N', 'b'] 意思是 a在b的北面（不一定是正北面）。 输出true/false， 满足这些条件的点存不存在。

类似于判断是否有环
'''
def check(l):
    record = {}
    def find(p1, p2):
        if p1 == p2:
            return True
        if p1 in record:
            for v in record[p1]:
                if find(v,p2):
                    return True
        return False
    for v in l:
        if v[1] == 'N':
            if not find(v[0],v[2]):
                record[v[2]] = record.get(v[2],[])
                record[v[2]].append(v[0])
            else:
                return False
        else:
            if not find(v[2],v[0]):
                record[v[0]] = record.get(v[0],[])
                record[v[0]].append(v[2])
            else:
                return False
    return True
if __name__ == '__main__':
    l = [['a','N','c'],['b','S','a'],['a','S','c']]
    print(check(l))