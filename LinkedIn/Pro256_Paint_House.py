'''
LinkedIn_Easy
10.12 11:59pm
'''
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        last_red = costs[0][0]
        last_blue = costs[0][1]
        last_green = costs[0][2]

        i = 1
        while i < len(costs):
            red = min(last_blue, last_green) + costs[i][0]
            blue = min(last_red, last_green) + costs[i][1]
            green = min(last_red, last_blue) + costs[i][2]

            last_red = red
            last_blue = blue
            last_green = green
            i += 1

        return min(last_red, last_blue, last_green)