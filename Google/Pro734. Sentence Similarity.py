'''
题意：
给了一堆similarity的法则要求找到words1和words2是不是same
法则不具有传递性，但有交换性

思路：
也可以用dict
'''
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        for i in range(len(words1)):
            if not(words1[i] == words2[i] or [words1[i],words2[i]] in pairs or [words2[i],words1[i]] in pairs):
                return False
        return True

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        l1 = len(words1)
        l2 = len(words2)
        if l1 != l2:
            return False
        d = dict()
        for p in pairs:
            if p[0] not in d:
                d[p[0]] = set()
            if p[1] not in d:
                d[p[1]] = set()
            d[p[0]].add(p[1])
            d[p[1]].add(p[0])
        for i in range(l1):
            if words1[i] == words2[i]:
                continue
            if words2[i] not in d:
                return False
            if words1[i] in d[words2[i]]:
                continue
            else:
                return False
        return True