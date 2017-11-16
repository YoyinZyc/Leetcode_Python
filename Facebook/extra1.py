def findone(start, end, s):
    i = 0
    while start <= end:
        middle = (start + end) // 2
        if s[middle] == 0:
            start = middle+1
        else:
            if middle == 0:
                break
            elif s[middle-1] == 0:
                i = middle
                break
            else:
                end = middle-1
    return i

def find_first_one(l):
    j = 1
    i = findone(0, len(l[0]) - 1, l[0])
    print(i)
    while j < len(l):
        if l[j][i] == 1:
            i = findone(0, i, l[j])
        j+=1
    return i

if __name__ == '__main__':
    l = [[0,0,1],[0,1,1],[0,0,0]]
    print(find_first_one(l))
