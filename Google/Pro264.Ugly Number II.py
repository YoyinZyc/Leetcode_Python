'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

DP
a：*2的位置
b: *3
c: *5

'''
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return []
        a = 0
        b = 0
        c = 0
        ret = [1]
        for i in range(1, n):
            ret.append(min(ret[a] * 2, ret[b] * 3, ret[c] * 5))
            # 注意这里不能用elseif，防止有相同值同时出现，都要+1，比如3*2和2*3
            if ret[-1] == ret[a] * 2:
                a += 1
            if ret[-1] == ret[b] * 3:
                b += 1
            if ret[-1] == ret[c] * 5:
                c += 1
        return ret[-1]

