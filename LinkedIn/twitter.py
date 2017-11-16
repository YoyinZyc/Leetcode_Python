# Enter your code here. Read input from STDIN. Print output to STDOUT
def mask_email(email_before):
    index_at = email_before.index('@')
    return email_before[0] + '*****' + email_before[index_at-1] + email_before[index_at:]
def mask_phone(phone_before):
    if phone_before[0] == '+':
        return '+' + mask_phone(phone_before[1:])
    else:
        phone_after = '***-***-' + phone_before[-4:]
        i = -5
        count = 0
        while i >= 0-len(phone_before) and count < 3:
            if phone_before[i].isdigit():
                count+=1
            i-=1
        count = 0
        while i >= 0-len(phone_before) and count<3:
            if phone_before[i].isdigit():
                count+=1
            i-=1
#Two situations: when there exists no char or '(' is the last char
        if i < 0-len(phone_before) or (phone_before[i] == '(' and i == 0-len(phone_before)):
            return phone_after
        phone_after = '-'+phone_after
        while i>= 0-len(phone_before):
            if phone_before[i].isdigit():
                phone_after = '*'+phone_after
            i-=1
        return phone_after

# oa3
# Complete the function below.


def maxLength(a, k):
    i = 0
    j = 0
    sum_suba = 0
    max_len = 0
    while i < len(a):
        sum_suba += a[i]
        if sum_suba > k:
            max_len = max(max_len, i - j)
            while sum_suba > k:
                sum_suba -= a[j]
                j += 1
        i += 1
    max_len = max_len = max(max_len, i - j)
    return max_len


if __name__ == '__main__':
    line = input()
    # print(input()[2] == ' ')
    while(line):
        if line[0] == 'E':
            print('E:'+mask_email(line[2:]))

        elif line[0] == 'P':
            print('P:'+ mask_phone(line[2:]))

        try:
            line = input()
        except EOFError:
            line = ''

