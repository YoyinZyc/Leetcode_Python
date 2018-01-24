# 题意：Input: S = "5F3Z-2e-9-w", K = 4
# Output: "5F3Z-2E9W"
# 所有小写字母要变成大写；dash把字符串分成多个group，除了第一个group，其余的group必须是K个字符

# 思路：
# 1.    可以先把所有字符都变成大写，并且把原字符串中的dash全都替换为空
# 2.    先把第一个group排除掉

# 从头开始
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # 变为大写，替换-
        S = S.upper().replace('-','')

        size = len(S)
        # 计算出第一个group的size
        s1 = K if size%K==0 else size%K
        # 把第一个group赋值给res
        res = S[:s1]
        # 从头向后添加组
        while s1<size:
            res += '-'+S[s1:s1+K]
            s1 += K
        return res

# 从末尾开始
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        i = len(S)
        ret = ''
        # 从后向前加
        while i > K:
            ret = '-' + S[i-K:i] +ret
            i-=K
        return S[:i]+ret