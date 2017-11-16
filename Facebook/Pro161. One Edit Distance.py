'''
Facebook_Medium
11.11 6:58pm
'''
class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        if abs(len(s) - len(t)) >= 2:
            return False

        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if len(s) == len(t):
                    return s[i + 1:] == t[j + 1:]
                elif len(s) > len(t):
                    return s[i + 1:] == t[j:]
                else:
                    return s[i:] == t[j + 1:]
        return True

