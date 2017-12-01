class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        ans = ''
        while n:
            ans = d[n%26] + ans
            if not n % 26:
                n = n//26-1
            else:
                n = n//26
        return ans