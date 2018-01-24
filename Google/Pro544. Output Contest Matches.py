'''
题意：
按照NBA比赛最强队和最弱队比较的规则，安排team match
Input: 8
Output: (((1,8),(4,5)),((2,7),(3,6)))
Explanation:
First round: (1,8),(2,7),(3,6),(4,5)
Second round: ((1,8),(4,5)),((2,7),(3,6))
Third round: (((1,8),(4,5)),((2,7),(3,6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).

思路：
递归
'''
class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        # n当前对数；m1和对手加起来的和，m2和对手加起来的和不能超过的数
        def helper(n, m1,m2):
            if m1 == m2:
                return '('+str(n)+','+str(m1-n)+')'
            return '(' + helper(n,(m1-1)*2+1,m2)  + ',' + helper(m1-n, (m1-1)*2+1, m2) + ')'

        return helper(1, 3, n+1)