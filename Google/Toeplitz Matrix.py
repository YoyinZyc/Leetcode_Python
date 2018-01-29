'''
Toepliz matrix:
左上到右下这条对角线上的数字相等

Input: mat[N][N] = {{ 6, 7, 8},
                    { 4, 6, 7},
                    { 1, 4, 6}},
Output : True;
Values in all diagonals are same.

Input: mat[N][N] = {{ 6, 7, 8, 9 },
                    { 4, 6, 7, 8 },
                    { 1, 4, 6, 7 },
                    { 0, 1, 4, 6 },
                    { 2, 0, 1, 4 }};
Output : True;

Input: mat[N][N] = {{ 6, 3, 8},
                    { 4, 9, 7},
                    { 1, 4, 6}},
Output : False;

'''
def Toeplitz(m):
    # 检查行
    for i in range(len(m)):
        x = i+1
        j = 1
        v = m[i][0]
        while x < len(m) and j < len(m[0]):
            if m[x][j] != v:
                return False
            x+=1
            j+=1
    # 检查列
    for i in range(1,len(m[0])):
        y = i+1
        j = 1
        v = m[0][i]
        while y < len(m[0]) and j < len(m):
            if m[j][y] != v:
                return False
            y+=1
            j+=1
    return True
if __name__ == '__main__':
    m = [[ 6, 7, 8, 9 ],
                    [ 4, 6, 7, 8 ],
                    [ 1, 4, 6, 7 ],
                    [ 0, 1, 4, 6 ],
                    [ 2, 0, 1, 4 ]];
    print(Toeplitz(m))
