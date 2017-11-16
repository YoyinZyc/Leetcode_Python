from queue import PriorityQueue
class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        if k == 0 or not points:
            return []
        q = PriorityQueue(maxsize = k)
        for p in points:
            q.put( ((((p.x - origin.x) ** 2 + (p.y - origin.y)**2) ** 0.5) , p.x, p) ,block=False)
        l = list()
        # i = 0
        while q:
            l.append(q.get()[2])
        return l
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
if __name__ == '__main__':
    p1 = Point(4,6)
    p2 = Point(4,7)
    p3 = Point(4,4)
    p4 = Point(2,5)
    p5 = Point(1,1)

    s = Solution()
    s.kClosest([p1,p2,p3,p4,p5], Point(0,0), 3)

