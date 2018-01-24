'''
水塘抽样问题
有N个元素的链表，事先不知道有多长，写一个函数可以高效地从其中取出k个随机数
從S中抽取首k項放入「水塘」中
對於每一個S[j]項（j ≥ k）：
   隨機產生一個範圍從0到j的整數r
   若 r < k 則把水塘中的第r項換成S[j]項
证明：
http://blog.csdn.net/my_jobs/article/details/48372399
'''
import random
def reservoir_Sampling(s, k):
    r = [0 for _ in range(k)]
    i = 0
    while i < k:
        r[i] = s[i]
        i+=1
    while i < len(s):
        p = random.randint(0,i)
        if p < k:
            r[p] = s[i]
        i+=1
    return r

if __name__ == '__main__':
    s = [1,2,3,4,5,6,8,9,0,12,32,45]
    print(reservoir_Sampling(s,5))