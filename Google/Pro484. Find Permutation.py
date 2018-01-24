'''
给一个string
D:代表decrease
I：代表increase
Input: "DI"
Output: [2,1,3]
要求找到字典序最小的组合

思路：
对于I：需要判断I之后的D有多少
    如果I有2个，D有3个，从1开始
    那就是1，2，6，5，4，3
    需要找到这个6
对于D：就是顺着分水岭往下减

特殊情况是当I是第一个，先要确定好首位肯定是1
'''
class Solution:
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        l = []
        i = 0
        # 如果I是第一个
        if s[0] == 'I':
            l.append(1)
        while i < len(s):
            # 开始的位置，因为从1开始且首位肯定被占用
            start = i + 2
            count_i = 0
            count_d = 0
            # 算多少个I
            while i < len(s) and s[i] == 'I':
                i += 1
                count_i += 1
            # 算多少个D
            while i < len(s) and s[i] == 'D':
                i += 1
                count_d += 1
            # 分水岭
            end = i + 1
            # I的最后一位是分水岭，所以到>1
            while count_i > 1:
                l.append(start)
                start += 1
                count_i -= 1
            l.append(end)
            # 到D
            while count_d > 0:
                l.append(end - 1)
                end -= 1
                count_d -= 1
        return l
