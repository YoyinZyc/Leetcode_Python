'''
典型的分治算法，将数组分成两个子数组，在子数组中继续拆分，
当小组只有一个数据时可认为有序，之后合并，所以重点就到了合并有序数组。

最差时间复杂度 Θ(n*logn)
平均时间复杂度 Θ(n*logn)
最优时间复杂度 Θ(n)
最差空间复杂度 Θ(n)

递归解法，temp参数是为了节约空间
stable not adaptive not in-place
'''


def sort(l):
    merge(l,0,len(l)-1,[0 for i in range(len(l))])
    print(l)
    return l
def merge(l,start,end, temp):
    if end>start:
        middle = (start+end)//2
        merge(l,start,middle,temp)
        merge(l,middle+1,end,temp)
        i = start
        j = middle+1
        k = 0
        while i < middle+1 and j < end+1:
            if l[i] <= l[j]:
                temp[k] = l[i]
                i+=1
            else:
                temp[k] = l[j]
                j+=1
            k+=1
        while i < middle+1:
            temp[k] = l[i]
            k+=1
            j+=1
        while j < end+1:
            temp[k] = l[j]
            j+=1
            k+=1
        for r in range(end-start+1):
            l[start+r] = temp[r]
