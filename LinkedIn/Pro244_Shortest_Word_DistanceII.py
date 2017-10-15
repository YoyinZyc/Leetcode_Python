'''
LinkedIn_Medium
10.12 11:43pm
'''

class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = dict()
        for i, v in enumerate(words):
            self.d[v] = self.d.get(v, list())
            self.d[v].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.d[word1]
        l2 = self.d[word2]
        distance = float('inf')
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            distance = min(distance, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return distance



        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)