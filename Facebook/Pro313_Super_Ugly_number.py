def nthUglyNumber(self, n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0


    while n > 1:
        # 先分别让2，3，5去乘
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        # 找到其中的最小的
        umin = min((u2, u3, u5))
        # 找到最小的对应的质数，把那个质数对应的坐标右移
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        indexes = [0 for _ in range(len(primes))]
        record = [0 for _ in range(n)]
        record[0] = 1
        j = 1
        while j < n:
            m = float('inf')
            for i,v in enumerate(primes):
                m = min(m, v*record[indexes[i]])
            for i,v in enumerate(indexes):
                if record[v] * primes[i] == m:
                    indexes[i]+=1
            record[j] = m
            j+=1
        return record[-1]