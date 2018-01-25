'''
Facebook_Easy
10.2 8:37pm
从1开始
1
11
21
1211
111221
循环比递归快
从空间复杂度和时间复杂度分析
'''
# 循环
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
# 递归
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n ==1 :
            return '1'
        ret = self.countAndSay(n-1)
        s = ''
        i = 0
        while i < len(ret):
            j = 1
            while i+j < len(ret) and ret[j+i] == ret[i]:
                j+=1
            s = s + str(j) + str(ret[i])
            i+=j
        return s




