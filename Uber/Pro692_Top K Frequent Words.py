'''
Uber_Medium
10.30 2:47pm
'''
# from queue import PriorityQueue
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words.sort()

        d1 = dict()
        d2 = dict()
        for v in words:
            if v in d1:
                d2[d1[v]].remove(v)
                if not d2[d1[v]]:
                    d2.pop(d1[v])
            d1[v] = d1.get(v, 0) + 1
            d2[d1[v]] = d2.get(d1[v], [])
            d2[d1[v]].append(v)
        ret = []
        i = 0
        while i < k:
            if not d2:
                return ret
            max_key = max(d2.keys())
            l = d2[max_key]
            j = 0
            while i < k and j < len(l):
                ret.append(l[j])
                i += 1
                j += 1
            d2.pop(max_key)
        return ret
