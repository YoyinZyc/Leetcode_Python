
'''
Facebook_Medium
10.8 9:53am
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s[0] == '0':
            return 0
        record = [0 for _ in range(len(s) + 1)]
        record[0] = 1
        record[1] = 1
        i = 2
        while i < len(s) + 1:
            if s[i - 1] == '0':
                if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                    record[i] = record[i - 2]
                else:
                    return 0
            else:
                if 11 <= int(s[i - 2] + s[i - 1]) <= 26:
                    record[i] = record[i - 1] + record[i - 2]
                else:
                    record[i] = record[i - 1]
            i += 1
        return record[-1]

