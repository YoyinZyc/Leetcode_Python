class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        count = 0
        one = 1
        two = 0
        for _ in range(n):
            one, two = one + two, one
        return one
