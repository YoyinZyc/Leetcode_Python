'''
LinkedIn_Easy
10.11 8:01pm
'''
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = dict()
        l = []
        for i in range(0, len(s) - 9):
            d[s[i:i + 10]] = d.get(s[i:i + 10], 0) + 1
            if d[s[i:i + 10]] == 2:
                l.append(s[i:i + 10])
        return l
