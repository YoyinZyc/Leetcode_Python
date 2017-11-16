'''
Facebook_Medium
11.05 12:18pm
'''
class Solution:
    def wordBreak(self, s, wordDict):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]
