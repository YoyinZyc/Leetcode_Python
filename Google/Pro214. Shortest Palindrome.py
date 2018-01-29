class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        def check(i, j):
            while i >= 0:
                if j >= len(s):
                    return False
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    return False
            return True

        i = (len(s) - 1) // 2
        while i >= 0:
            if s[i] == s[i + 1]:
                if (check(i - 1, i + 2)):
                    return s[i + 2:][::-1] + s[i] + s[i + 1] + s[i + 2:]

            if (check(i - 1, i + 1)):
                return s[i + 1:][::-1] + s[i] + s[i + 1:]
            i -= 1

'''
思路2：
利用KMP算法
把s变成 s+'#'+s[::-1]
这样相当于求这个s的部分匹配表，求最长的相同的前缀后缀

复杂度为O(n)

KMP算法：
http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
'''
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = [0]
        new_s = s+'#'+s[::-1]
        for i in range(1,len(new_s)):
            t = table[-1]
            # 如果不同一直往前面找
            while t>0  and new_s[i] != s[t]:
                t = table[t-1]
            # 要判断是不是0，如果是append 0
            if new_s[i] == s[t]:
                table.append(t+1)
            else:
                table.append(0)
        return s[table[-1]:][::-1] + s

if __name__ == '__main__':
    s = Solution()
    s.shortestPalindrome('babbbabbaba')