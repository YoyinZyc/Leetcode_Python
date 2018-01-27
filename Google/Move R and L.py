'''
有一个source string，一个 target string。二者都只包含 "L","R","_" 三种字符，L可以往 左移，R可以往右移，不能 jump over。
让设计一个函数，判断 能否从source走到target，返回
boolean

思路：
第二题我的想法，定义两个变量num_L. num_R记录L和R出现的个数，
同时loop source和target，由于source里的L只能向左，R只能向右，
所以同时loop时一定是target里先遇到L（或者同时遇到），
且一定是source里先遇到R（或者同时遇到），所以loop时遇到target[i]为L,
则num_L加一， 如果source[i]为L， 则num_L减一，如果source[i]是R，则num_R加一，
如果target[i]是R，则num_R减一。若任意时刻出现num_L<0 或num_R<0，
说明source走不到target，return False。这样O(n)就搞定了。
'''
def move(source, target):
    if len(source) != len(target):
        return False
    # 记录source中多的L，可以左移和target匹配
    num_L = 0
    # 记录target中多的R，可以右移和source匹配
    num_R = 0
    i = 0
    while i < len(source):
        if source[i] != target[i]:
            if source[i] == 'L':
                if not num_L:
                    return False
                else:
                    num_L-=1
            if source[i] == 'R':
                num_R+=1

            if target[i] == 'R':
                if not num_R:
                    return False
                else:
                    num_R-=1
            if target[i] == 'L':
                num_L+=1
        i+=1
    return not num_R and not num_L
if __name__ == '__main__':
    print(move('_L_R','___R'))
