class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(area**0.5)
        l = mid
        while area % l:
            l-=1
        return [area//l,l]