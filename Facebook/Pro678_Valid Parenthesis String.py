'''
Facebook_Medium
11.4 11:47
'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0
        for i in range(len(s)):
            if s[i] == '(':
                low += 1
                high += 1
            elif s[i] == ')':
                if low > 0:
                    low -= 1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            if high < 0:
                return False

        return low == 0

# Solution 2
from collections import deque


# class Solution:
#     def checkValidString(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s1 = deque()
#         s2 = deque()
#
#         for i in range(len(s)):
#             if s[i] == '(':
#                 s1.append(i)
#             elif s[i] == ')':
#                 if not s1 and not s2:
#                     return False
#                 if not s1:
#                     s2.pop()
#                 else:
#                     if s[s1[-1]] == '(':
#                         s1.pop()
#                     else:
#                         s1.append(i)
#             else:
#                 s2.append(i)
#         while s1:
#             if not s2:
#                 return False
#             if s1[-1] < s2[-1]:
#                 s1.pop()
#                 s2.pop()
#             else:
#                 return False
#
#         return True