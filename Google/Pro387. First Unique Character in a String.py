'''
找到String中第一个unique char的位置

思路：
用Orderdict
dict的读取查询速度快
'''
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = OrderedDict()
        for i,v in enumerate(s):
            record[v] = record.get(v,[])
            record[v].append(i)
        while record:
            l = record.popitem(last=False)
            if len(l[1]) == 1:
                return l[1][0]
        return -1