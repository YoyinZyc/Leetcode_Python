class Solution(object):
    def numDecodings(self, S):
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in S:
            if c == '*':
                e0, e1, e2 = (9*e0 + 9*e1 + 6*e2)%MOD, e0, e0
            else:
                e0, e1, e2 = ((c > '0') * e0 + e1 + (c <= '6') * e2) %MOD, (c == '1') * e0, (c == '2') * e0
        return e0