'''
Google_Easy
10.9 10:23pm
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l = [0, 0]
        for v in moves:
            if v == 'U':
                l[0] += 1
            elif v == 'D':
                l[0] -= 1
            elif v == 'L':
                l[1] -= 1
            else:
                l[1] += 1
        if l == [0, 0]:
            return True
        return False

