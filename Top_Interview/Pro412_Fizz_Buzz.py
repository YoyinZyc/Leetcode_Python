'''
Top_Interview_Easy
9.18 10:21am
'''


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # l = [i for i in range(1,n+1)]
        l = []
        for i in range (1, n+1):
            if i % 15 == 0:
                l.append('FuzzBuzz')
            elif i %3 == 0:
                l.append('Fuzz')
            elif i%5==0:
                l.append('Buzz')
            else:
                l.append(i)
        return l