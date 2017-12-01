class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for v in strs:
            key = [0 for _ in range(26)]
            for c in v:
                key[ord(c)-ord('a')] += 1
            key = tuple(key)
            if key in d:
                d[key].append(v)
            else:
                d[key] = [v]
        return list(d.values())


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        d = dict()
        for v in strs:
            key = 1
            for c in v:
                key *= primes[ord(c) - ord('a')]
            if key in d:
                d[key].append(v)
            else:
                d[key] = [v]
        return list(d.values())
