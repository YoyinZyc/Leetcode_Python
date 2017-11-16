'''
Facebook_Hard
11.07 3:25pm
'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k:
            return 0
        if len(prices) <= 1:
            return 0
        if k > len(prices) // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

        l_hold = [-float('inf') for _ in range(k)]
        l_release = [0 for _ in range(k)]
        for i, v in enumerate(prices):
            for j in range(min(i // 2, k - 1), 0, -1):
                l_release[j] = max(l_release[j], l_hold[j] + v)
                l_hold[j] = max(l_hold[j], l_release[j - 1] - v)
            l_release[0] = max(l_release[0], l_hold[0] + v)
            l_hold[0] = max(l_hold[0], 0 - v)
        return max(l_release)