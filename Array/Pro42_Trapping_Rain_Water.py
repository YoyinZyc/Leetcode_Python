'''
Array_Hard
9.14 11:04pm
'''

from  collections import  deque
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        heightIndex = deque()
        area = 0
        for i, h in enumerate(height):

            if not heightIndex:
                heightIndex.append(i)
            else:
                peek = heightIndex[-1]

                if h == height[peek]:
                    heightIndex.pop()
                elif h > height[peek]:
                    bottom = height[heightIndex.pop()]
                    while heightIndex:
                        if height[heightIndex[-1]] <= h:
                            area += (height[heightIndex[-1]]-bottom) * (i-heightIndex[-1]-1)
                            bottom = height[heightIndex.pop()]
                        else:
                            area +=(h -bottom) * (i-heightIndex[-1]-1)
                            break
                heightIndex.append(i)
        return  area