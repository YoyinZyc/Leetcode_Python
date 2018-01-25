'''
21点游戏.
牌只有1-10点，如果还没满17点就要再拿一张，问超过21点的机率是多少？
DP问题，但面试时太紧张，不知道怎么设定DP，尤其是被一直抽牌有好几轮迷惑了。
最后面试官提示，只要用DP计算拿到我点的机率，然后1-（P（17 ）+ P（18）+ P（19）+ P（20）+ P（21））就好，还是太浅了我
牌无限拿，可放回
'''
def points():
    dp = [0.1]
    for i in range(1,10):
        dp.append(0.1 + sum(dp) / 10)
    for i in range(10,16):
        dp.append(sum(dp[i-10:])/10)
    for i in range(16,21):
        dp.append(sum(dp[i-10:16])/10)
    return 1-(dp[16]+dp[17]+dp[18]+dp[19]+dp[20])
if __name__ == '__main__':
    print(points())