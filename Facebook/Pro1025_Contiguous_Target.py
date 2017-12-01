def find_target(list, t):
    s = list[0]
    i = 1
    j = 0
    while i < len(list):
        if s == t:
            return True
        if list[i]-list[i-1] == 1:
            s += list[i]
        else:
            while j < i:
                s -= list[j]
                if s == t:
                    return True
                j+=1
            s += list[i]
        i+=1
    return False
if __name__ == '__main__':
    print(find_target([0,1,2,4,7,8],9))