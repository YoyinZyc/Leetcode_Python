'''
题意：
734的升级版，允许传递性，判断两个sentence是不是similar
1. Union Find
2. DFS
'''
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # Union find
        parent = {}

        def find(w):
            if w not in parent:
                parent[w] = w
            if parent[w] == w:
                return w
            return find(parent[w])
        # 构造union
        def union(a, b):
            a1 = find(a)
            b1 = find(b)
            parent[a1] = b1

        for a, b in pairs:
            union(a, b)

        l1, l2 = len(words1), len(words2)
        if l1 != l2:
            return False

        for i in range(l1):
            if words1[i] == words2[i]:
                continue
            a, b = find(words1[i]), find(words2[i])
            if a != b:
                return False

        return True

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        d = dict()
        for v in pairs:
            d[v[0]] = d.get(v[0],set())
            d[v[0]].add(v[1])
            d[v[1]] = d.get(v[1],set())
            d[v[1]].add(v[0])
        def check(path,w1,w2):
            if w1 == w2:
                return True
            if w1 not in d or w2 not in d:
                return False
            for v in d[w1]:
                if v not in path:
                    if check(path+[v],v,w2):
                        return True
            return False
        for i in range(len(words1)):
            if not check([words1[i]],words1[i], words2[i]):
                return False
        return True