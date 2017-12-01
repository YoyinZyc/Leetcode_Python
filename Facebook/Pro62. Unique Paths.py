class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        record = [1 for _ in range(n)]
        i = 1
        while i < m:
            j = 1
            while j < n:
                record[j] += record[j-1]
                j+=1
            i+=1
        return record[-1]