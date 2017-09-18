'''
Top_Interview_Easy
9.18 12:09pm
'''

from collections import deque
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = deque()
        record = deque()
        for i in range(len(s)):
            if s[i] in record:
                if s[i] in q:
                    q.remove(s[i])
            else:
                q.append(s[i])
            record.append(s[i])
        if q:
            u = q.popleft()
            for i,v in enumerate(record):
                if v == u:
                    return i
        else:
            return -1