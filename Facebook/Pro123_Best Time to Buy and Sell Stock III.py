'''
Facebook_Hard
11:4 7:13pm
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        prices.insert(0, float('inf'))
        once_pro = 0
        twice_pro = 0
        once_min = 1
        dp = {1: [0, 0, 1]}
        index_l = [1]
        i = 2
        while i < len(prices):
            if prices[i] < prices[i - 1]:
                while i < len(prices) and prices[i] <= prices[i - 1]:
                    i += 1
                if prices[i - 1] < prices[once_min]:
                    once_min = i - 1
                dp[i - 1] = [once_pro, twice_pro, once_min]
                index_l.append(i - 1)
            else:
                while i < len(prices) and prices[i] >= prices[i - 1]:
                    i += 1
                for index in index_l:
                    twice_pro = max(twice_pro, prices[i - 1] - prices[index] + dp[index][0])
                if once_pro < prices[i - 1] - prices[once_min]:
                    once_pro = prices[i - 1] - prices[once_min]
        return max(twice_pro, once_pro)

