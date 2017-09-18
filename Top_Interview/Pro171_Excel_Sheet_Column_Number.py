'''
Top_Interview_Easy
9.17 11:00pm
'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        ret = 0
        while i < len(s):
            ret += (ord(s[-1-i])-ord('A')+1) * pow(26,i)
            i+=1
        return  ret