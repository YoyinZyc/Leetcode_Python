from collections import OrderedDict
def custom_sort(alp,str):
    d= OrderedDict()
    for v in alp:
        d[v] = 0
    for v in str:
        d[v] += 1
    ret = ''
    while d:
        e = d.popitem(last=False)
        ret += e[0] * e[1]
    return ret
if __name__ == '__main__':
    print(custom_sort('xyzabc','cyxz'))