
'''
Amazon_Medium
10.9 11:43am
'''
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        F = [0]
        n = len(A)
        for i in range(0, n):
            F[0] += i * A[i]
        j = 1
        sum_A = sum(A)

        while j < n:
            F.append(F[j - 1] + sum_A - A[0 - j] * n)
            j += 1
        return max(F)