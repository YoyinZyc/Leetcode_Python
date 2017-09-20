'''
堆节点的访问

通常堆是通过一维数组来实现的。在数组起始为 0 的情形中，如果 i 为当前节点的索引，则有

父节点在位置 floor((i-1)/2)；
左子节点在位置 (2*i+1)；
右子节点在位置 (2*i+2)；

堆的操作

在堆的数据结构中，堆中的最大值总是位于根节点。堆中定义以下几种操作：

最大堆调整（Max-Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点，保持最大堆性质的关键。运行时间为 O(lg n)。
创建最大堆（Build-Max-Heap）：在无序的输入数组基础上构造出最大堆。运行时间为 O(n)。
堆排序（HeapSort）：对一个数组进行原地排序，卸载位在第一个数据的根节点，并做最大堆调整的递归运算。运行时间为 O(n*lg n)。
抽取最大值（Extract-Max）：相当于执行一次最大堆调整，最大值在根处。运行时间为 O(lg n)。

最差时间复杂度 O(n*logn)
平均时间复杂度 Θ(n*logn)
最优时间复杂度 O(n*logn)
最差空间复杂度 O(n)，辅助空间 O(1)

not stable not adaptive
'''
def build_max_heap(l, size):
    i = (size-1)//2
    while i>=0:
        max_heapify(l, i,size)
        i-=1



def max_heapify(l, i, size):
    if i <= size//2-1:
        left = i * 2 + 1
        right = i * 2 + 2
        maxIndex = i
        if l[left] > l[maxIndex]:
            maxIndex = left

        if right < size and l[right] > l[maxIndex]:
            maxIndex = right
        if maxIndex != i:
            temp = l[i]
            l[i] = l[maxIndex]
            l[maxIndex] = temp
            max_heapify(l, maxIndex, size)
def sort(l):
    build_max_heap(l, len(l))
    for i in range(len(l)-1,-1,-1):
        temp = l[0]
        l[0] = l[i]
        l[i] = temp
        max_heapify(l, 0, i)
    print(l)
