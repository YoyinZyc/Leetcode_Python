'''
Facebook_Hard
11.11 4:44pm
'''
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        points = []
        for v in buildings:
            points.append([v[0], 0 - v[2]])
            points.append([v[1], v[2]])
        points.sort()
        height = [0]
        prev = 0
        for p in points:
            if p[1] < 0:
                self.insert_h(height, p[1])
            else:
                height.remove(0 - p[1])
            cur = height[0]
            if prev != cur:
                result.append([p[0], 0 - cur])
                prev = cur
        return result

    def insert_h(self, height, h):
        if height[0] >= h:
            height.insert(0, h)
            return
        if height[-1] <= h:
            height.append(h)
            return

        start = 1
        end = len(height) - 1
        while start <= end:
            middle = (start + end) // 2
            if height[middle] == h:
                height.insert(middle, h)
                return
            elif height[middle] < h:
                if height[middle + 1] >= h:
                    height.insert(middle + 1, h)
                    return
                else:
                    start = middle + 1
            else:
                if height[middle - 1] < h:
                    height.insert(middle, h)
                    return
                else:
                    end = middle - 1
