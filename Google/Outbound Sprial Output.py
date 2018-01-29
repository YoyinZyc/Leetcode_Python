'''
题意：
給一個String 用outbound spiral方式輸出 (ex. abcde -> cdbae)

思路：
先中
然后右左左右为一个周期
'''
def output(l):
    center = l[len(l)//2]
    print(center)
    i = len(l)//2-1
    j = len(l)//2+1
    while j < len(l) or i >= 0:
        if j < len(l):
            print(l[j])
            j+=1
        if i >= 0:
            print(l[i])
            i-=1
        if i >= 0:
            print(l[i])
            i-=1
        if j < len(l):
            print(l[j])
            j+=1
if __name__ == '__main__':
    output([1,3,0,9,8])