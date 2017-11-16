'''
Facebook_Medium
11.5 8:25pm
'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        s2 = sorted(s)
        for i in range(0, len(s)):
            if s[i] == s2[-1-i]:
                i+=1
            else:
                j = len(s)-1
                while j > i:
                    if s[j] == s2[-1-i]:
                        return int(s[:i] +s[j] + s[i+1:j] + s[i] + s[j+1:])
                    j-=1
        return num