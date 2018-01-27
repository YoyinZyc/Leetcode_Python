from collections import deque
import numpy as np
'''
题意：解决数独
'''

'''
方法1：
backtracking
'''
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.helper(board,0)
    def helper(self, board, posi):
        # 如果81个cell遍历完了
        if posi >= 81:
            return True
        i = posi // 9
        j = posi % 9
        # 如果是'.'
        if board[i][j] == '.':
            # 把1-9依次放进去试
            for n in range(1,10):
                if self.check(board,i,j,str(n)):
                    board[i][j] = str(n)
                    # 如果剩下的也满足，返回true
                    if self.helper(board,posi+1):
                        return True
                    board[i][j] = '.'

            return False
        # 如果是数字，直接下一个
        else:
            return self.helper(board,posi+1)

    # 检查这个数字放进去之后可不可以
    def check(self,board, x,y,num):
        for i in range(9):
            if board[x][i] == num:
                return False
        for i in range(9):
            if board[i][y] == num:
                return False
        for i in range(3 * (x//3),3 * (x//3)+3):
            for j in range(3 * (y//3),3 * (y//3)+3):
                if board[i][j] == num:
                    return False
        return True
'''
Dancing Links
可是，直观上面的规则，发现比较难以转换为精确覆盖问题。因此，把上面的表述换个说法

1、每个格子只能填一个数字

2、每行1-9的这9个数字都得填一遍（也就意味着每个数字只能填一遍）

3、每列1-9的这9个数字都得填一遍

4、每宫1-9的这9个数字都得填一遍

http://www.cnblogs.com/grenet/p/3163550.html
http://www.cnblogs.com/grenet/p/3145800.html
复杂，但是速度快

'''
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        Head = Cell(-1, -1, 0)
        cell = Head
        last_cell_of_col = []
        counts = np.zeros(9 * 9 * 4)
        headers = []
        for i in range(9 * 9 * 4):
            cell.right = Cell(-1, i, 0)
            cell.right.left = cell
            cell = cell.right
            last_cell_of_col.append(cell)
            headers.append(cell)
        cell.right = Head
        Head.left = cell

        count_r = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(9):
                        c1 = Cell(count_r, i*9+j, k+1, header= headers[i*9+j], row_in_b=  i , col_in_b=j)
                        last_cell_of_col[i*9+j].down = c1
                        c1.up = last_cell_of_col[i * 9 + j]
                        last_cell_of_col[i * 9 + j] = c1
                        counts[i*9+j] += 1

                        c2 = Cell(count_r, 81+i*9+k, k+1, header = headers[81+i*9+k], row_in_b=  i , col_in_b=j)
                        last_cell_of_col[81+i*9+k].down = c2
                        c2.up = last_cell_of_col[81+i*9+k]
                        last_cell_of_col[81+i*9+k] = c2
                        counts[81+i*9+k] += 1

                        c3 = Cell(count_r, 81*2+j*9+k, k+1,row_in_b=  i , col_in_b=j, header= headers[81*2+j*9+k])
                        last_cell_of_col[81*2 + j * 9 + k].down = c3
                        c3.up = last_cell_of_col[81*2 + j * 9 + k]
                        last_cell_of_col[81*2 + j * 9 + k] = c3
                        counts[81*2+j*9+k] += 1

                        c4 = Cell(count_r, 81*3 + (i//3 * 3 + j//3)*9 + k , k+1, row_in_b=  i , col_in_b=j, header=headers[81*3 + (i//3 * 3 + j//3)*9 + k ])
                        last_cell_of_col[81*3 + (i//3 * 3 + j//3)*9 + k].down = c4
                        c4.up = last_cell_of_col[81*3 + (i//3 * 3 + j//3)*9 + k]
                        last_cell_of_col[81*3 + (i//3 * 3 + j//3)*9 + k] = c4
                        counts[81*3 + (i//3 * 3 + j//3)*9 + k] += 1
                        c1.right = c2
                        c2.left = c1
                        c2.right = c3
                        c3.left = c2
                        c3.right = c4
                        c4.left = c3
                        c4.right = c1
                        c1.left = c4
                        count_r+=1
                else:
                    k = int(board[i][j]) - 1

                    c1 = Cell(count_r, i * 9 + j, k + 1, header=headers[i * 9 + j], row_in_b=i, col_in_b=j)
                    last_cell_of_col[i * 9 + j].down = c1
                    c1.up = last_cell_of_col[i * 9 + j]
                    last_cell_of_col[i * 9 + j] = c1
                    counts[i * 9 + j] += 1

                    c2 = Cell(count_r, 81 + i * 9 + k, k + 1, header=headers[81 + i * 9 + k], row_in_b=i, col_in_b=j)
                    last_cell_of_col[81 + i * 9 + k].down = c2
                    c2.up = last_cell_of_col[81 + i * 9 + k]
                    last_cell_of_col[81 + i * 9 + k] = c2
                    counts[81 + i * 9 + k] += 1

                    c3 = Cell(count_r, 81 * 2 + j * 9 + k, k + 1, row_in_b=i, col_in_b=j,
                              header=headers[81 * 2 + j * 9 + k])
                    last_cell_of_col[81 * 2 + j * 9 + k].down = c3
                    c3.up = last_cell_of_col[81 * 2 + j * 9 + k]
                    last_cell_of_col[81 * 2 + j * 9 + k] = c3
                    counts[81 * 2 + j * 9 + k] += 1

                    c4 = Cell(count_r, 81 * 3 + (i // 3 * 3 + j // 3) * 9 + k, k + 1, row_in_b=i, col_in_b=j,
                              header=headers[81 * 3 + (i // 3 * 3 + j // 3) * 9 + k])
                    last_cell_of_col[81 * 3 + (i // 3 * 3 + j // 3) * 9 + k].down = c4
                    c4.up = last_cell_of_col[81 * 3 + (i // 3 * 3 + j // 3) * 9 + k]
                    last_cell_of_col[81 * 3 + (i // 3 * 3 + j // 3) * 9 + k] = c4
                    counts[81 * 3 + (i // 3 * 3 + j // 3) * 9 + k] += 1
                    c1.right = c2
                    c2.left = c1
                    c2.right = c3
                    c3.left = c2
                    c3.right = c4
                    c4.left = c3
                    c4.right = c1
                    c1.left = c4
                    count_r+=1
        for i, v in enumerate(headers):
            v.up = last_cell_of_col[i]
            last_cell_of_col[i].down = v
            v.count = counts[i]
        print(count_r)
        self.dancing(Head, headers, board)
        print(board)
    def dancing(self, Head, headers, board):
        col1 = min(headers, key=lambda x: x.count)
        if not col1.count:
            return []
        removed_col = deque()
        self.remove(col1, headers)
        ans = []
        row = col1.down
        while row.row != -1:
            row_start = row.right
            while row_start.col != row.col:
                # print('remove second:' + str(row_start.header.col))
                self.remove(row_start.header, headers)
                removed_col.append(row_start.header)
                row_start = row_start.right
            if Head.right == Head:
                board[row.row_in_b][row.col_in_b] = str(row.val)
                return True
            else:
                ret = self.dancing(Head, headers, board)
                if (ret):
                    board[row.row_in_b][row.col_in_b] = str(row.val)
                    return True
                else:
                    self.resume(removed_col, headers)
            row = row.down
        q = deque()
        q.append(col1)
        self.resume(q, headers)
        return False

    def remove(self, col, headers):
        # if col.col < self.board.area:
        headers.remove(col)
        col.left.right = col.right
        col.right.left = col.left

        col = col.down
        while col.row != -1:
            row_start = col.right
            while row_start.col != col.col:
                # print(row_start.header)
                row_start.header.count -= 1
                # print(str(row_start.header.col) + ' remove  ' + str(row_start.header.count))
                row_start.up.down = row_start.down
                row_start.down.up = row_start.up
                row_start = row_start.right
            col = col.down

    def resume(self, remove_col, headers):
        # self.headers.append(col)
        while remove_col:
            col = remove_col.pop()
            col = col.up
            while col.row != -1:
                row_start = col.left
                while row_start.col != col.col:
                    row_start.header.count += 1
                    # print(str(row_start.header.col) + ' resume  ' + str(row_start.header.count))
                    row_start.up.down = row_start
                    row_start.down.up = row_start
                    row_start = row_start.left
                col = col.up
            col.left.right = col
            col.right.left = col
            # self.headers.append(col)
            # if col.col < self.board.area:
            headers.append(col)


class Cell(object):
    def __init__(self, row, col, val, count=0, header=None, row_in_b = 0, col_in_b = 0):
        self.row = row
        self.col = col
        self.val = val
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.row_in_b = row_in_b
        self.col_in_b = col_in_b
        self.count = count
        self.header = header


if __name__ == '__main__':
    s = Solution()
    s.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])