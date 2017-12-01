'''
在数据集之中，选择一个元素作为”基准”（pivot）。
所有小于”基准”的元素，都移到”基准”的左边；所有大于”基准”的元素，都移到”基准”的右边。
这个操作称为分区 (partition) 操作，分区操作结束后，基准元素所处的位置就是最终排序后它的位置。
对”基准”左边和右边的两个子集，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。

最差时间复杂度 O(n2)
平均时间复杂度 O(n*log n)
最优时间复杂度 O(n*log n)
最差空间复杂度 根据实现的方式不同而不同 O(n) 辅助空间 O(log n)

not stable
'''



def sort(l):
    quickSort(l,0,len(l)-1)
    print(l)
def quickSort(l, start, end):
    if start >= end:
        return
    low = start
    high = end
    pivot = l[end]
    while start < end:
        if l[start] > pivot:
            end-=1
            l[start], l[end] = l[end], l[start]
        else:
            start+=1
    l[start], l[high] = l[high], l[start]
    quickSort(l, low, start-1)
    quickSort(l, start+1, high)
    # if end > start:
    #     pivot = l[end]
    #     j = start
    #     i = start
    #     while i < end:
    #         while j < end and l[j]<=pivot:
    #             j+=1
    #         if j == end:
    #             break
    #         if j == end-1:
    #
    #             break
    #
    #         i = max(j+1,i)
    #         if l[i] <= pivot:
    #
    #             temp = l[i]
    #             l[i] = l[j]
    #             l[j] = temp
    #             j+=1
    #         i+=1
    #     temp = l[j]
    #     l[j] = l[end]
    #     l[end] = temp
    #     quickSort(l, start, j-1)
    #     quickSort(l, j+1,end)
