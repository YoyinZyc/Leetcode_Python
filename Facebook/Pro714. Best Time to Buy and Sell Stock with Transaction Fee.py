class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = -float('inf')
        sell = 0
        for v in prices:
            buy = max(sell - v - fee, buy)
            sell = max(sell, buy + v)
        return sell
