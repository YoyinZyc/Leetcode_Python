'''
Facebook_Hard
11.8 11:57pm
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
from collections import deque


class Solution(object):
    def __init__(self):
        self.q = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n and self.q:
            buf[i] = self.q.popleft()
            i += 1
        if i == n:
            return n
        while i < n:
            temp = ['' for _ in range(4)]
            get_read = read4(temp)
            if get_read > n - i:
                j = 0
                while j < n - i:
                    buf[i + j] = temp[j]
                    j += 1
                while j < get_read:
                    self.q.append(temp[j])
                    j += 1
                return n
            if get_read < 4:
                j = 0
                while j < get_read:
                    buf[i + j] = temp[j]
                    j += 1
                return i + get_read
            for j in range(4):
                buf[i + j] = temp[j]
            i += 4
        return n



