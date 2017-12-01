class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        i = 1
        while i < len(costs):
            j = 0
            first_min = min(costs[i-1])
            min_loc = costs[i-1].index(first_min)
            second_min = min(costs[i-1][:min_loc]+costs[i-1][min_loc+1:])
            while j < len(costs[0]):
                if costs[i-1][j] == first_min:
                    costs[i][j] += second_min
                else:
                    costs[i][j] += first_min
                j+=1
            i+=1
        return min(costs[-1])