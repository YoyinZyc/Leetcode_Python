'''
Pro72 Edit Distance
w1[i] = w2[j]
dp[i,j] = dp[i-1][j-1]
w1[i] !=w2[j]: dp[i,j] = min(dp[i-1,j-1],dp[i-1,j],d[[i,j-1])+1
为了防止边缘过届，可以现在边上加上一层，record变成（m+1)(n+1）
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 有空
        if not word1 or not word2:
            return max(len(word1),len(word2))
        record = [[0 for _ in range(len(word1)+1)]for _ in range(len(word2)+1)]
        # 第一行   0-m
        for i in range(1,len(word1)+1):
            record[0][i] = i
        # 第一列   0-n
        for i in range(1,len(word2)+1):
            record[i][0] = i
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word2[i] == word1[j]:
                    record[i+1][j+1] = record[i][j]
                else:
                    record[i+1][j+1] = min(record[i][j],record[i][j+1],record[i+1][j])+1
        return record[-1][-1]