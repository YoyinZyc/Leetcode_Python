'''
Top_Interview_Easy
9.18 10:00pm
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')
