# Given a sorted list of numbers, reduce the list by adding duplicate numbers
# 比如：1 2 2 3 -> 1 4 3，要求inplace，two pointers就能解决
def reduce(l):
    i = 0
    while i < len(l)-1:
        if l[i+1] != l[i]:
            i+=1
            continue
        j = 1
        while i+j < len(l) and l[i+j] == l[i]:
            j+=1
        l[i] = j * l[i]
        l = l[:i+1]+l[i+j:]
    return l
if __name__ == '__main__':
    print(reduce([1,1,1,2,2,3]))