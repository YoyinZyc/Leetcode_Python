'''
Facebook_Easy
10.2 4:56pm
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        num = 0
        while i < len(s) - 1:
            v1 = d[s[i]]
            v2 = d[s[i + 1]]
            if v1 < v2:
                num += v2 - v1
                i += 1
            else:
                num += v1
            i += 1
        if i < len(s):
            num += d[s[-1]]
        return num

