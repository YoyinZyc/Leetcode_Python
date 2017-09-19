'''
奇偶排序通过比较数组中相邻的（奇-偶）位置元素，如果该奇偶元素对是错误的顺序（前者大于后者），
则交换元素。然后再针对所有的（偶-奇）位置元素进行比较。如此交替进行下去。
最差时间复杂度 O(n2)
平均时间复杂度 O(n2)
最优时间复杂度 O(n)
最差空间复杂度 О(1)
adaptive
stable
'''
def sort(l):
    for i in range(len(l)):
        if i % 2 == 0:
            for j in range(1,len(l),2):
                if l[j] < l[j-1]:
                    temp = l[j]
                    l[j] = l[j-1]
                    l[j-1] = temp
        else:
            for j in range(2,len(l),2):
                if l[j] < l[j-1]:
                    temp = l[j]
                    l[j] = l[j-1]
                    l[j-1] = temp
    print(l)