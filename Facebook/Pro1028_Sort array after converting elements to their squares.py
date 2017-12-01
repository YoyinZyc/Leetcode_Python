def sort_square(l):
    begin = 1
    end = len(l)-1
    center = 0
    while begin <= end:
        mid = (begin+end) // 2
        if l[mid] >= 0 and l[mid-1] < 0:
            center = mid
            break
        elif l[mid] >= 0:
            end = mid-1
        else:
            begin = mid+1
    i = center -1
    j = center
    ret = []
    while i >= 0 and j <len(l):
        if abs(l[i]) < abs(l[j]):
            ret.append(l[i]**2)
            i-=1
        else:
            ret.append(l[j]**2)
            j+=1
    while i >= 0:
        ret.append(l[i]**2)
        i-=1
    while j < len(l):
        ret.append(l[j] ** 2)
        j+=1
    return ret
if __name__ == '__main__':
    ret = sort_square([-6,-3,-2,3,5,8,9])
    print(ret)