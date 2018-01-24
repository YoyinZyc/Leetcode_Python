'''
group 一组string
'abc'，'bcd'这种就是一组

思路：
用map
重点是算key，一组的string，每个word每个字符和前一个字符的差形成的一个list 是相同的
'''
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for v in strings:
            key = []
            for i in range(1, len(v)):
                # 要%26 因为会有负数
                key.append((ord(v[i]) - ord(v[i - 1])) % 26)
            key = tuple(key)
            d[key] = d.get(key, [])
            d[key].append(v)
        return list(d.values())
