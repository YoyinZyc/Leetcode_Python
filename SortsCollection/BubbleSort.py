'''
O(n^2)
冒泡排序对 n 个元素需要 O(n2) 的比较次数，且可以原地排序。冒泡排序仅适用于对于含有较少元素的数列进行排序。

最差时间复杂度 O(n2)
平均时间复杂度 O(n2)
最优时间复杂度 O(n)
最差空间复杂度 O(n)，辅助空间 O(1)
Stable
O(1) extra space
O(n^2^) comparisons and swaps
Adaptive: O(n) when nearly sorted
'''
class BubbleSort(object):
    def __init__(self, l):
        self.l = l


    def sort(self):
        for i in range(len(self.l)):
            for j in range(1,len(self.l)-i):
                if self.l[j-1]> self.l[j]:
                    temp = self.l[j]
                    self.l[j] = self.l[j-1]
                    self.l[j-1] = temp
        print (self.l)

