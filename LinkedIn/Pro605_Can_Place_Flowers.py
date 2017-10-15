'''
LinkedIn_Medium
10.12 3:08pm
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed) and n:
            if flowerbed[i] == 1:
                i+=2
            else:
                if i == len(flowerbed)-1:
                    n-=1
                    break
                if flowerbed[i+1] == 1:
                    i += 3
                else:
                    n-=1
                    i+=2
        if n:
            return False
        return True