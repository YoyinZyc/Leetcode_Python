'''

问了一道题

给一个数组，n的长度（n >=1），含有所有1 - n的数字，
要求得到一个最小的index，满足条件: 如果把数组小于等于index的部分排序好，
并且把数组大于index的部分排序好，那么整个数组就排序好了。

看题目可能有点绕，以下是当时给的两个examples：
3 1 2 5 4
返回的index为2，即如果(3,1,2)和(5,4)分别排序完成，那么整个数组就排序好了。

2 4 3 1
返回的index为3

思路：
1.用count
2.求和，如果一个点满足，那么他的和一定是1-n的，如果和大于，必定还要在后面
'''
def find_index(l):
    index = l[0]
    count = l[0]-1
    for i in range(1,len(l)):
        # 如果l[i]比之前的index大，更新index和count
        if l[i] > index:
            count = l[i] - index + count
            index = l[i]
        count-=1
        if not count:
            return index-1
    return index-1
if __name__ == '__main__':
    print(find_index([2,4,3,1]))
