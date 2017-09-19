'''
Top_Interview_Easy
9.18 3:39pm
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        if x == 1:
            return 1


        start = 0
        end = x

        while end-start>1:
            middle = (start+end)//2
            if pow(middle,2) == x:
                return  middle
            elif pow(middle,2) < x:
                start = middle
            else:
                end = middle
        return start


