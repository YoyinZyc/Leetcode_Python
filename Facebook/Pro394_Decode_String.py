from collections import deque


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        stack = deque()
        for v in s:
            if v != ']':
                stack.append(v)
            else:
                # 找word
                word = ''
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()
                # 找数字
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append((int)(num) * word)
        return ''.join(stack)
