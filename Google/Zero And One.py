'''
0变01，1变10。第0行是0，第一行是01，第二行是0110，第三行01101001。。。
一直下去问求第k行第j个数是什么，递归Ologj时间On空间搞定拍照走人
k行的第j个和k-1行的第j//2相关
'''
def zero_and_one(k, j):
    if k == 0:
        return 0
    ret = zero_and_one(k-1, j//2)
    if j % 2:
        if ret == 1:
            return 0
        else:
            return 1
    else:
        if ret == 1:
            return 1
        else:
            return 0
if __name__ == '__main__':
    print(zero_and_one(3,1))