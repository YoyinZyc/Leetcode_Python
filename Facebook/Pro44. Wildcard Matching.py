'''
Facebook_Hard
11.10 9:48pm
'''
# 方法1：DP
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        record = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        record[0][0] = True
        i = 0
        while i < len(p) and p[i] == '*':
            record[0][i + 1] = True
            i += 1
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '?':
                    record[i + 1][j + 1] = record[i][j]
                elif p[j] == '*':
                    record[i + 1][j + 1] = record[i + 1][j] or record[i][j] or record[i][j + 1]
        return record[-1][-1]


# 方法2：Constant space
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = 0
        starIndex = -1
        p_i = 0
        s_i = 0

        while s_i < len(s):
            if p_i < len(p) and (p[p_i] == '?' or p[p_i] == s[s_i]):
                p_i += 1
                s_i += 1
            elif p_i < len(p) and p[p_i] == '*':
                starIndex = p_i
                match = s_i
                p_i += 1
            elif starIndex != -1:
                p_i = starIndex + 1
                match += 1
                s_i = match
            else:
                return False

        while p_i < len(p) and p[p_i] == '*':
            p_i += 1
        return p_i == len(p)
if __name__ == '__main__':
    s = Solution()
    s.isMatch('iecdfide', 'i*de')