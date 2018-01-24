'''
题意：
给了一个string和一个dict
要求把String中出现的dict中词汇都加上<br></br>的标签

如果有重合，要merge
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

思路：
先转换为一堆intervals
然后就是merge intervals的题
'''
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        record = []
        # 外层循环是s，这样就不用sort这个record了
        for i in range(len(s)):
            for v in dict:
                if s[i:i + len(v)] == v:
                    record.append([i, i + len(v)])

        i = 1
        while i < len(record):
            # 如果重合
            if record[i][0] >= record[i - 1][0] and record[i][0] <= record[i - 1][1]:
                record[i - 1][1] = max(record[i - 1][1], record[i][1])
                record.pop(i)
            else:
                i += 1
        l = []
        # 记录上一次结束的位置
        last_end = 0
        for v in record:
            # 加上没有加bold的词汇
            l.append(s[last_end:v[0]])
            # 加bold
            l.append('<b>' + s[v[0]:v[1]] + '</b>')
            # 改变last_end
            last_end = v[1]
        # 最后还要加上没有加bold的部分
        l.append(s[last_end:])
        # 最后join在一起
        return ''.join(l)