'''
Uber_Medium
10.30 11:51pm
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_s = set(s)
        if len(set_s) == 1:
            return len(s)
        record = [[1 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if i + 1 == j:
                        record[i][j] = 2
                    else:
                        record[i][j] = record[i + 1][j - 1] + 2
                else:
                    record[i][j] = max(record[i + 1][j], record[i][j - 1])
        return record[0][len(s) - 1]