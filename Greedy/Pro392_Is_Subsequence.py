'''
Greedy_Medium
9.12 8:42pm
'''


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i = i+1
                j = j+1
            else:
                j = j+1
        if i== len(s):
            return  True
        return  False