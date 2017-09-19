'''
每次取一个元素插入正确的位置，适合少量元素。对于未排序的数据，从已排序的序列中从后向前扫描，找到相应的位置插入，
实现上通常使用 in-place 排序，只需要使用额外 O(1) 空间，但是因为插入正确的位置之后，需要反复移动已经排序的序列，
为新元素提供插入空间，因而比较费时。
In-Place 原地排序（即只需要用到 O(1) 的额外空间）
最差时间复杂度 O(n2)
平均时间复杂度 O(n2)
最优时间复杂度 O(n)
最差空间复杂度 O(n)，辅助空间 O(1)

Stable
O(1) extra space
O(n^2^) comparisons and swaps
Adaptive: O(n) time when nearly sorted
Very low overhead

但我这里用的应该是半插入，即是用来binary search，就不一定是稳定的了
'''
def sort(l):
    for i in range(1,len(l)):
        if l[i] <= l[0]:
            temp = l[i]
            j = i
            while(j >= 1):
                l[j] = l[j-1]
                j-=1
            l[0] = temp
        elif l[i] < l[i-1]:
            start = 0
            end = i-1
            while end-start > 1:
                middle = (end+start)/2
                if l[middle] > l[i]:
                    end = middle
                elif l[middle] < l[i]:
                    start = middle
                else:
                    end = middle
                    break
            temp = l[i]
            j = i
            while (j >= end+1):
                l[j] = l[j-1]
                j-=1
            l[end] = temp
    print(l)

