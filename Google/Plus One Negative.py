'''
题意：
有负数的plus one
注意-1，要去掉负号
'''
def plus(num):
    if num == ['-','1']:
        return 0
    if num[0] == '-':
        carry = -1
        for i in range(len(num)-1, 0, -1):
            num[i] = int(num[i]) + carry
            carry = num[i] // 10
            num[i] = str(num[i] % 10)
        if num[1] == '0':
            return ['-'] + num[2:]
        return num
    else:
        carry = 1
        for i in range(len(num)-1, -1, -1):
            num[i] = int(num[i]) + carry
            carry = num[i] // 10
            num[i] = str(num[i] % 10)
        if carry:
            return ['1']+num
        return num
if __name__ == '__main__':
    print(plus(['9','9']))
