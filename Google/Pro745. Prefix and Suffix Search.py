'''
题意：
有一堆word
给了一个prefix和一个suffix，要求找到对应的word，且满足条件的word的index最大

思路：
两个方法：
Trie：会超时
dict：因为word最多只有10个字符长，所以可以用；使用dict节省读取时间
'''
class WordFilter(object):

    def __init__(self, words):
        self.inputs = {}
        # 对于每个word
        for index, word in enumerate(words):
            prefix = ''
            # 遍历word
            for char in [''] + list(word):
                # 前缀
                prefix += char
                suffix = ''
                # 遍历后缀
                for char in [''] + list(word[::-1]):
                    suffix += char
                    # 是index，如果有key相同，更新value
                    self.inputs[prefix + '.' + suffix[::-1]] = index
    # 直接读取
    def f(self, prefix, suffix):
        return self.inputs.get(prefix + '.' + suffix, -1)


class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        # 两个Trie树
        self.pre_t = Trie()
        self.suf_t = Trie()
        # 创建
        for i, v in enumerate(words):
            self.pre_t.add(v, i)
            self.suf_t.add(v[::-1], i)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        # 读取prefix对应的
        t1 = self.pre_t
        for v in prefix:
            if v in t1.next:
                t1 = t1.next[v]
            else:
                return -1
        # 读取suffix对应的
        t2 = self.suf_t
        for v in suffix[::-1]:
            if v in t2.next:
                t2 = t2.next[v]
            else:
                return -1
        # 取交集，max
        return max(t1.ws & t2.ws)


class Trie(object):
    def __init__(self):
        self.next = dict()
        self.ws = set()

    def add(self, word, i):
        self.ws.add(i)
        if not word:
            return
        if word[0] in self.next:
            self.next[word[0]].add(word[1:], i)
        else:
            self.next[word[0]] = Trie()
            self.next[word[0]].add(word[1:], i)

            # Your WordFilter object will be instantiated and called as such:
            # obj = WordFilter(words)
            # param_1 = obj.f(prefix,suffix)