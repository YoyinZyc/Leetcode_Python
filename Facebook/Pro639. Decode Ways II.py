'''
Facebook_Hard
11.5 10:33am
'''
class Solution(object):
    def numDecodings(self, S):
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in S:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0