class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        end = max(L)
        start = 1
        while start <= end:
            mid = (start + end) // 2
            if self.count(L, mid) >= k:
                start = mid + 1
            else:
                end = mid - 1
        return end

    def count(self, L, length):
        c = 0
        for v in L:
            c += (v // length)
        return c