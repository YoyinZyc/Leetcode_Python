'''
Facebook_Medium
10.7 7:14pm
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        ret = [0 for _ in range(m + n)]
        i = -1
        while i > -1 - m:
            v1 = int(num1[i])
            j = -1
            k = i
            while j > -1 - n:
                v2 = int(num2[j])
                p = v1 * v2
                ret[k] = ret[k] + p
                if ret[k] >= 10:
                    ret[k - 1] += ret[k] // 10
                    ret[k] = ret[k] % 10
                k -= 1
                j -= 1
            i -= 1
        i = 0
        while ret[i] == 0:
            i += 1
        return ''.join(map(str, ret[i:]))


