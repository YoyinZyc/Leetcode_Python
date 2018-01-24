'''
题意：
把python的下划线命名法转变为java的驼峰式
'''
def convert(p):
    l = p.split('_')
    if len(l) == 1:
        return p
    for i in range(1,len(l)):
        l[i] = l[i].capitalize()
    return ''.join(l)
if __name__ == '__main__':
    print(convert('op_yu_l'))