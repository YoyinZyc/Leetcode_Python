'''
Facebook_Easy
10.2 8:37pm
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        laststr = '1'
        i = 1
        while i < n:
            s = str()
            v = laststr[0]
            j = 1
            count = 1
            while j < len(laststr):
                if laststr[j] != v:
                    s = s + str(count) + v
                    count = 1
                    v = laststr[j]
                else:
                    count += 1
                j += 1
            laststr = s + str(count) + v
            i += 1
        return laststr




