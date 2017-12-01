def mul(a,b):
    l_a = []
    l_b = []
    res = 0
    for i in range(len(a)):
        if a[i]:
            l_a.append((i,a[i]))
        if b[i]:
            l_b.append((i,b[i]))

    def find_in_b(loc):
        start = 0
        end = len(l_b)
        while start<=end:
            mid = (start+end)//2
            if l_b[mid][0] == loc:
                return l_b[mid][1]
            elif l_b[mid][0] < loc:
                start = mid+1
            else:
                end = mid-1
        return 0
    for v in l_a:
        res += find_in_b(v[0]) * v[1]
    return res
if __name__ == '__main__':
    print(mul([0,0,0,0,1,2,0,4],[1,7,0,2,0,0,3,1]))




