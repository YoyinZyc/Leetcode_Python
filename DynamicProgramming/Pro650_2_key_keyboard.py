'''
DP_Medium
9.21 2:20pm
'''

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        primes = [2,3,5,7,11,13,17,19,23,29,31,37]
        i = 0
        count = 0
        while i < len(primes) and n > 1:
            while n % primes[i] == 0:
                count += primes[i]
                n = n/primes[i]
            i+=1
        if n != 1:
            count+=n
        return count