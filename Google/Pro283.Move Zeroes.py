# 需要相对位置，相当于用一个新的pointer记录list
# 不需要相对位置
def move_zeros(l):
    i = 0
    j = len(l)-1
    while i < j:
        if l[i] == 0 and l[j] != 0:
            l[i] = l[j]
            l[j] = 0
        if l[i] != 0:
            i+=1
        if l[j] == 0:
            j-=1
    print(l)
    
# 需要相对位置，相当于用一个新的pointer记录list
def move_zeros_origin(l):
    i = 0
    j = 0
    while i < len(l) and l[i]:
        i+=1
    j = i
    while i < len(l):
        if l[i]:
            l[j] = l[i]
            j+=1
        i+=1
    while j < len(l):
        l[j] = 0
        j+=1
    print(l)
if __name__ == '__main__':
    move_zeros([0,1,0,1,3])
    move_zeros_origin([0,1,0,1,3])