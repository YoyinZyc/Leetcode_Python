'''
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
原地操作几乎是选择排序的唯一优点，当空间复杂度（space complexity）要求较高时，可以考虑选择排序，实际适用的场合非常罕见。

最差时间复杂度 О(n²)
平均时间复杂度 О(n²)
最优时间复杂度 О(n²)
最差空间复杂度 О(n)，辅助空间 O(1)
not stable
not adaptive
'''
def sort(l):
    for i in range(len(l)):
        index = 0
        for j in range(1,len(l)-i):
            if l[j] > l[index]:
                index = j
        if len(l)-i-1 != index:
            temp = l[index]
            l[index] = l[len(l)-i-1]
            l[len(l)-i-1] = temp
    print(l)