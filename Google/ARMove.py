'''
一个车，可以收两个指令A和R。A就向前走一秒然后速度加倍。R就停下来然后反向。给一个AR组成的string求最后停在哪里。
反问如果给位置求string。
'''
# 正常的增减
def ARMove(l,inispeed):
    speed = inispeed
    posi = 0
    direction = True
    for v in l:
        if v == 'A':
            if direction:
                posi += speed
            else:
                posi -= speed
            speed = speed << 1
        else:
            direction = not direction
            speed = inispeed
    return posi
# 反向的话用greedy，先找到A最多的个数，然后反向把距离终点剩下的位置走完，直到到达终点
def reverse(posi):
    if posi < 0:
        return ['R'] + reverse(-posi)
    if not posi:
        return []
    start = 0
    end = 10
    while start < end:
        mid = (start + end) // 2
        if posi > 2**mid - 1:
            start += 1
        else:
            end -= 1
    return ['A'] * end + ['R']+ reverse(2**end-1-posi)
if __name__ == '__main__':
    print(ARMove(['A','A','A','R','A'],1))
    print(reverse(-6))