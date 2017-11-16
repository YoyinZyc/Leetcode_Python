class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d1 = dict()
        d2 = dict()
        max_t = 1
        for v in tasks:
            d1[v] = d1.get(v,0)+1
            d2[d1[v]] = d2.get(d1[v],0)+1
            max_t = max(max_t,d1[v])
        return max((max_t-1) * (n+1) + d2[max_t], len(tasks))