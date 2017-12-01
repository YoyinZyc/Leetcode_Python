from collections import deque


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = deque()
        s = path.split('/')
        for v in s:
            if v and v != '.':
                if v == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(v)
        sim_p = '/'.join(list(stack))
        return '/' + sim_p

