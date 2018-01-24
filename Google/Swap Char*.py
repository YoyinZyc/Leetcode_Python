'''
两字符串，问其中一个里面交
换两个字母的位置能不能得到
另外一个
'''
def swapToB(s1,s2):
    # 长度不同肯定False
    if len(s1) != len(s2):
        return False
    i = 0
    pos1 = -1
    pos2 = -1
    # 找到第一个不同的地方
    while i < len(s1):
        if s1[i] != s2[i]:
            pos1 = i
            break
        i+=1
    i+=1
    # 找到第二个不同的地方
    while i < len(s1):
        if s1[i] != s2[i]:
            pos2 = i
            break
        i+=1
    # 只有一个不同或者没有不同：False
    if pos1 == -1 or pos2 == -1:
        return False
    # 可以交换，True
    if s1[pos1] == s2[pos2] and s2[pos1] == s1[pos2]:
        return True
    return False
'''
Follow up
如果允许交换n次
则要求两个字符串对于同一个字符要有相同的个数
'''
def swapN(s1,s2):
    if len(s1) != len(s2):
        return False
    record = [0 for _ in range(26)]
    i = 0
    while i < len(s1):
        record[ord(s1[i])-ord('a')] += 1
        record[ord(s2[i]) - ord('a')] -= 1
        i+=1
    # 用any
    return not any(record)

if __name__ == '__main__':
    print(swapToB('hjkl','ljkl'))
    print(swapN('jjjkkki','kikkjjj'))