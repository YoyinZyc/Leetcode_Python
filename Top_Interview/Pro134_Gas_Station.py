class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1
        remain = [gas[i] - cost[i] for i in range(len(gas))]

        start_i = remain.index(max(remain))

        i = start_i - len(gas)
        while i < start_i:
            j = i
            remain_gas = 0
            while j < start_i:
                remain_gas += remain[j]
                if remain_gas < 0:
                    break
                j += 1
            if j == start_i:
                if i < 0:
                    return i + len(gas)
                else:
                    return i
            i = j
            while i < start_i and remain[i] < 0:
                i += 1

        return -1



