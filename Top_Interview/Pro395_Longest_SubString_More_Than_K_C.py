'''
Top_Interview_Medium
10:15 11:37pm
'''
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        max_l = 0
        a_l = set(s)
        for v in a_l:
            if s.count(v) < k:
                s_l = s.split(v)
                for v in s_l:
                    max_l = max(max_l, self.longestSubstring(v, k))
                return max_l
        return len(s)

