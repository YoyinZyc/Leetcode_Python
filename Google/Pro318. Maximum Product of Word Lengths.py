'''
题意：
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn"
要求这两个word中的字符不能有重复

思路：
bit_manipulation 与运算
把每一个word转换为bit
注意一个word钟有重复字符的情况，要用set去重
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = []
        max_p = 0
        for i in range(len(words)):
            l.append(len(words[i]))
            # 去重
            words[i] = set(words[i])
            n = 0
            # 转换为数字
            for v in words[i]:
                n += 2 ** (ord(v) - ord('a'))
            words[i] = n

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not words[i] & words[j]:
                    max_p = max(max_p, l[i] * l[j])
        return max_p


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for word in words:
            mask = 0
            for c in set(word):
                # 右移
                mask |= (1 << (ord(c) - ord('a')))
            d[mask] = max(d.get(mask,0), len(word))
        return max([d[x]* d[y] for x in d for y in d if not x & y] or [0])