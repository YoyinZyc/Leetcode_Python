'''
题意：
要求找到所有长度为n的这种数字

思路：
用11，88，69，96来包围n-2的结果
'''
class Solution:
    def findStrobogrammatic(self, n):
        def helper(m, n):
            # n<2的两种特殊情况
            if m == 0: return [""]
            if m == 1: return ["0", "1", "8"]
            tmp = helper(m - 2, n)
            res = []
            for i in range(len(tmp)):
                # 如果m=n，说明首位不能为0，不能用00来包围
                if m != n: res.append("0" + tmp[i] + "0")
                # 用69，96，11，88来包围
                res.append("1" + tmp[i] + "1")
                res.append("6" + tmp[i] + "9")
                res.append("8" + tmp[i] + "8")
                res.append("9" + tmp[i] + "6")
            return res
        return helper(n, n)