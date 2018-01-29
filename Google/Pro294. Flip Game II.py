'''
接上题的flip游戏
判断先手是否一定能赢

这种游戏对于两个人是一样的

思路：
backtracking
或者dp+dict
'''
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        n = len(s)
        memo = dict()
        def win(s):
            # 如果s没有在memo中，递归去找s的情况
            if s not in memo:
                memo[s] = False
                for i in range(len(s) - 1):
                    if s[i:i+2] == '++':
                        # 如果下一个人不能赢，只要有一个情况下一个人不能赢，memo[s]就是true
                        if not win(s[:i] + '--' + s[i+2:]):
                            memo[s] = True
                            break
            return memo[s]
        return win(s)