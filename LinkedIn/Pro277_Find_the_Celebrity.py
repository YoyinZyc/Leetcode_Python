'''
LinkedIn_Medium
10.11 10:35pm
先找到可能的celebrity，再验证
'''

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = [[0 for _ in range(n)] for _ in range(n)]

        i = 0
        while i < n:
            j = 0
            while j < n:
                if j != i:
                    if knows(i, j):
                        record[i][j] = 1
                        break
                    else:
                        record[i][j] = -1
                j += 1
            if j == n:
                k = 0
                while k < n:
                    if not record[k][i]:
                        if not knows(k, i):
                            return -1
                    else:
                        if record[k][i] == -1:
                            return -1
                    k += 1
                return i
            i += 1
        return -1





