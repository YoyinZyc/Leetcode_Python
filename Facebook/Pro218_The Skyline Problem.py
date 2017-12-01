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
        # 对于每一个building，把（左节点，负的高度）（右节点，正的高度）加入point
        for v in buildings:
            points.append([v[0], 0 - v[2]])
            points.append([v[1], v[2]])
        # 按照左节点sort
        points.sort()
        height = [0]
        prev = 0
        # 对于每一个节点
        for p in points:
            # 如果p[1]小于0说明是左节点，把高度插入height中
            if p[1] < 0:
                self.insert_h(height, p[1])
            else:
                # 如果是右节点，把height中对应的左节点删去
                height.remove(0 - p[1])
            # 如果当前height中最小的值和前一次最小的值不同
            cur = height[0]
            if prev != cur:
                # 把最前面的值以及当前的坐标一起存入result
                result.append([p[0], 0 - cur])
                # 改变prev
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
