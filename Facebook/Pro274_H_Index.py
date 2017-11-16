class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        record = [0 for _ in range(len(citations)+1)]
        for v in citations:
            if v > len(citations):
                record[len(citations)] += 1
            else:
                record[v] += 1
        total = 0
        for i in range(len(citations), -1, -1):
            total += record[i]
            if total >= i:
                return i
        return 0