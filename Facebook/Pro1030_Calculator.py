from collections import deque
def pop_cal(stack1, stack2):
    n2 = stack2.pop()
    n1 = stack2.pop()
    op = stack1.pop()
    result = 0
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    else:
        result = n1*n2
    stack2.append(result)
def calculate(e):
    tokens = []
    i = 0
    while i < len(e):
        v = e[i]
        if v == ' ':
            continue
        if v == '*':
            tokens.append('*')
        elif v == '+':
            tokens.append('+')
        elif v == '-':
            tokens.append('-')
        elif v == ')':
            tokens.append(')')
        elif v == '(':
            tokens.append('(')
        else:
            num = ''
            while i < len(e) and e[i].isdigit():
                num += e[i]
                i+=1
            tokens.append(num)
            i-=1
        i+=1
    #     operator
    stack1 = deque()
    #     number
    stack2 = deque()
    for v in tokens:
        if not stack1:
            stack1.append(v)
        elif v == '(':
            stack1.append('(')
        elif v == ')':
            while stack1[-1] != '(':
                pop_cal(stack1,stack2)
            stack1.pop()
        elif v == '+' or v == '-':
            while stack1 and (stack1[-1] == '+' or stack1[-1] == '-' or stack1[-1] == '*' or stack1[-1] == '/'):
                pop_cal(stack1,stack2)
            stack1.append(v)
        elif v == '*' or v == '/':
            while stack1 and (stack1[-1] == '*' or stack1[-1] == '/'):
                pop_cal(stack1,stack2)
            stack1.append(v)
    while stack1:
        pop_cal(stack1,stack2)
    return stack2.pop()
