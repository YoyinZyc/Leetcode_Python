class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        record = [0 for _ in range(128)]
        for v in t:
            record[ord(v)] += 1
        end = 0
        begin = 0
        count = len(t)
        min_window = float('inf')
        head = 0
        while end < len(s):
            record[ord(s[end])] -= 1
            if record[ord(s[end])] >= 0:
                count -= 1
            end += 1
            while not count:
                if end - begin < min_window:
                    min_window = end - begin
                    head = begin
                record[ord(s[begin])] += 1
                if record[ord(s[begin])] > 0:
                    count += 1
                begin += 1
        if min_window == float('inf'):
            return ''
        return s[head:head + min_window]

