'''
Greedy_Easy
9.12 9:43pm
'''


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points.sort()
        p1 = points[0]
        count = 1
        for i in range(1, len(points)):
            p1 = self.helper(p1, points[i])
            if p1==False:
                count+=1
                p1 = points[i]

        return count
    def helper(self, p1, p2):
        if p2[0] > p1[1]:
            return  False
        return [min(p1[0],p2[0]),min(p1[1], p2[1])]