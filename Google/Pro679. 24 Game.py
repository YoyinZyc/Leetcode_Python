'''
+ - * / ( )算24点
先得到排列组合
然后分两种情况
有括号和没有
要注意精度问题
sys.float_info.epsilon
'''

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        comb = []
        # 组合
        def combination(prev, last):
            if not last:
                comb.append(prev)
            for i, v in enumerate(last):
                combination(prev + [v], last[:i] + last[i + 1:])

        combination([], nums)

        def helper(ns, target):
            # 精度判断
            if len(ns) == 1:
                return abs(ns[0] - target) <= sys.float_info.epsilon
            n1 = ns[0]
            n2 = ns[1]
            # 没有括号 的加减乘除
            if helper(ns[1:], target - n1):
                return True
            if helper(ns[1:], n1 - target):
                return True
            if n1 and target:
                if helper(ns[1:], target / n1):
                    return True
                    # if target:
                if helper(ns[1:], n1 / target):
                    return True
            # 有括号的加减乘除
            if helper([n1 + n2] + ns[2:], target):
                return True
            if helper([n1 - n2] + ns[2:], target):
                return True
            if helper([n1 * n2] + ns[2:], target):
                return True
            if n2:
                if helper([n1 / n2] + ns[2:], target):
                    return True
            return False

        for v in comb:
            if helper(v, 24.0):
                return True
        return False
if __name__ == '__main__':
    s = Solution()
    print(s.judgePoint24([5,5,1,5]))

# class Solution(object):
#     def judgePoint24(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         comb = []
#
#         def combination(prev, last):
#             if not last:
#                 comb.append(prev)
#             for i, v in enumerate(last):
#                 combination(prev + [v], last[:i] + last[i + 1:])
#
#         combination([], nums)
#
#         def helper(ns):
#             if len(ns) == 1:
#                 return [ns[0]]
#             ret = []
#             n1 = ns[0]
#             n2 = ns[1]
#             r1 = helper(ns[1:])
#             for v in r1:
#                 ret.append(n1 + v)
#                 ret.append(n1 - v)
#                 ret.append(n1 * v)
#                 if v:
#                     ret.append(n1 / v)
#             ret += helper([n1 + n2] + ns[2:])
#             ret += helper([n1 - n2] + ns[2:])
#             ret += helper([n1 * n2] + ns[2:])
#             if n2:
#                 ret += helper([n1 / n2] + ns[2:])
#             return ret
#
#         for v in comb:
#             ret = helper(v)
#             if 24 in ret:
#                 return True
#         return False