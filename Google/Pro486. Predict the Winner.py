'''
题意：
两个玩家，每个玩家可以从当前数列的首尾选一个数字，不可放回
要求看player1可不可以是winner

平局也算winner

思路：
DP
bottom-up
up-down
'''
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n, 1):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = dict()
        def helper(i,j,p):
            if i == j:
                if p:
                    record[(i,j)] = (nums[i],0)
                else:
                    record[(i,j)] = (0, nums[i])
            if (i,j) in record:
                return record[(i,j)]
            if p:
                c1 = helper(i+1,j,False)
                c2 = helper(i,j-1,False)
                if c1[0]+nums[i]-c1[1] > c2[0] + nums[j] - c2[1]:
                    record[(i,j)] = (c1[0]+nums[i],c1[1])
                else:
                    record[(i,j)] = (c2[0] + nums[j],c2[1])
            else:
                c1 = helper(i+1,j,True)
                c2 = helper(i,j-1,True)
                if c1[1]+nums[i]-c1[0] > c2[1] + nums[j] - c2[0]:
                    record[(i,j)] = (c1[0], c1[1]+nums[i])
                else:
                    record[(i,j)] = (c2[0],c2[1] + nums[j])
            return record[(i,j)]
        helper(0,len(nums)-1,True)
        if record[(0,len(nums)-1)][0] >= record[(0,len(nums)-1)][1]:
            return True
        return False