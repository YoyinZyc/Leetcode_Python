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
            if v1 == 0:
                i -= 1
                continue
            j = -1

            count = 0
            while j > -1 - n:
                v2 = int(num2[j])
                if v2 == 0:
                    count += 1
                    j -= 1
                    continue
                p = v1 * v2
                p1 = p % 10
                p2 = p // 10
                k = i - count
                while ret[k] + p1 >= 10:
                    ret[k] = ret[k] + p1 - 10
                    k -= 1
                    p1 = 1
                ret[k] = ret[k] + p1
                k = i - count

                while ret[k - 1] + p2 >= 10:
                    ret[k - 1] = ret[k - 1] + p2 - 10
                    k -= 1
                    p2 = 1
                ret[k - 1] = ret[k - 1] + p2
                count += 1
                j -= 1
            i -= 1
        print(ret)
        ret_s = str()
        i = 0
        while ret[i] == 0:
            i += 1
        while i < len(ret):
            ret_s += str(ret[i])
            i += 1
        return ret_s


