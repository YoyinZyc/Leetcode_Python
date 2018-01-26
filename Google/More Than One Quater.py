'''
给定一个sorted array 找出出现次数超过总数四分之一元素。
如果是小数，取整。比如长度为五，那么超过一次就可以。

思路：
往中间平均切三个点，然后用二分法分别check这三个点的左右边界
'''
def check(l):
    # 间距是除以4的上届
    interval = (len(l)+3) // 4
    ret = []
    # 切点
    p = [l[interval-1], l[2 * interval - 1],l[3 * interval-1]]
    # 二分分别找这三个点的上下届
    for v in p:
        start = 0
        end = len(l)-1
        while start <= end:
            mid = (start+end)//2
            if l[mid] < v:
                start = mid+1
            else:
                end = mid-1
        down = start
        start = 0
        end = len(l) - 1
        while start <= end:
            mid = (start + end) // 2
            if l[mid] > v:
                end = mid - 1
            else:
                start = mid + 1
        up = end
        if up-down+1 >= interval:
            ret.append(l[down])
    return ret
if __name__ == '__main__':
    print(check([1,1,1,2,3,4,4,5,8,10]))
