class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = -float('inf')
        sell = 0
        cool = 0
        for v in prices:
            last_cool = cool
            cool = max(cool, sell, buy)
            sell = max(sell, buy+v)
            buy = max(last_cool-v, buy)
        return sell