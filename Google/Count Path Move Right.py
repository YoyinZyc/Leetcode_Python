'''
 dp题。给一个grid的宽和长，求得从左下的点到右下的点所有可能的路径之和。
起点当然是左下，要求每次只能走三个方向， ➡↗↘

dp[i][j] = dp[i-1][j-1]+dp[i+1][j-1]+dp[i][j-1]

followup:用1D?不会
'''
