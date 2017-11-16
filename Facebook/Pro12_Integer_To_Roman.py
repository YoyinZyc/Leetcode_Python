'''
Facebook_Medium
11.2 5:12pm
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {2:['C','D','M'], 1:['X','L','C'], 0:['I','V','X'] }
        ret = ""
        for i in range(num //1000):
            ret += 'M'
        num = num % 1000
        for i in range(2,-1,-1):
            n = num // (10 ** i)
            ret += self.getValue(n, d[i])
            num = num % (10 ** i)
        return ret
    def getValue(self,v, l):
        if v == 0:
            return ''
        elif v == 1:
            return l[0]
        elif v == 2:
            return l[0]+l[0]
        elif v == 3:
            return l[0]+l[0]+l[0]
        elif v == 4:
            return l[0]+l[1]
        elif v == 5:
            return l[1]
        elif v ==6:
            return l[1]+l[0]
        elif v == 7:
            return l[1]+l[0]+l[0]
        elif v == 8:
            return l[1]+l[0]+l[0]+l[0]
        elif v == 9:
            return l[0]+l[2]