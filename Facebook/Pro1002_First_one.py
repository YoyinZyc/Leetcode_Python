def find_first_one(l,j):
    start = 0
    end = j
    while start <= end:
        mid = (start+end) // 2
        if l[mid] == 1:
            end = mid-1
        else:
            start = mid+1
    return start
def find_one(ls):
    i = 0
    end = len(ls[0])-1
    while i < len(ls):
        if i == 0 or ls[i][end] == 1:
            end = find_first_one(ls[i], end)
        i+=1
    return end
if __name__ == '__main__':
    print(find_one([[0,0,0,1,1],[0,1,1,1,1],[1,1,1,1,1]]))

