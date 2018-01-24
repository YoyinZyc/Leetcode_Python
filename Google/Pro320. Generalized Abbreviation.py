'''
题意：
求出一个单词的所有abbr
思路：
递归
'''
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        # 如果word是空，返回这个
        if not word:
            return [""]
        l = []
        # 递归求解word[1:]
        ret = self.generateAbbreviations(word[1:])
        for v in ret:
            i = 0
            # 求出返回值String中作为数字的前几位
            while i < len(v) and v[i].isdigit():
                i += 1
            # 如果开头没有数字
            if v[:i]:
                num = int(v[:i])
                # 数字+1
                l.append(str(num + 1) + v[i:])
                # word[0] +v
                l.append(word[0] + v)
            else:
                # '1'
                l.append('1' + v)
                # word[0] + v
                l.append(word[0] + v)
        return l


