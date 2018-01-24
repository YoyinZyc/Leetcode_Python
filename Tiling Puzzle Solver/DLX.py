from DataGenerator import DataGenerator
from collections import deque
import numpy
import time

class Cell(object):
    def __init__(self, row, col, count = 0, header = None):
        self.row = row
        self.col = col
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.count = count
        self.header = header

    def set_left(self, Cell):
        self.left = Cell

    def set_right(self, Cell):
        self.right = Cell

    def set_up(self, Cell):
        self.up = Cell

    def set_down(self, Cell):
        self.down = Cell

class DLX(object):
    # record = []
    def __init__(self, file_path, rotate = False, flip_h = False):
        data_generator = DataGenerator(file_path)
        self.board = data_generator.board
        self.tiles = data_generator.tiles
        self.tile_size = len(self.tiles)
        self.board_length = len(self.board.tile)
        self.board_width = len(self.board.tile[0])
        self.count_one = []
        self.headers = []
        if rotate and flip_h:
            self.matrix = self.create_matrix_fhr()
        elif rotate:
            self.matrix = self.create_matrix_r()
        elif flip_h:
            self.matrix = self.create_matrix_fh()
        else:
            self.matrix = self.create_matrix()
        # print(self.matrix)
        # fo = open('output.txt','w')
        # for v1 in self.matrix:
        #     for v2 in v1:
        #         fo.write(str(v2))
        #         fo.write("\t")
        #
        #     fo.write("\n")
        # fo.close()
        Head = self.create_DL(self.matrix)
        # head_right = Head.right
        matrix_zip = list(zip(*self.matrix))
        for i in range(len(matrix_zip)):
            self.headers[i].count = matrix_zip[i].count(1)
            # self.count_one.append(head_right.count)
            # self.headers.append(head_right)
        self.headers = self.headers[:self.board.area]
        self.t0 = time.time()
        self.solutions = self.dancing1(Head)
        t1 = time.time()
        print("It cost %f sec" % (t1-self.t0))
        print(self.solutions)
        print(len(self.solutions))
        # print(self.dancing(Head))
        # print(matrix)


    def create_matrix_fhr(self):
        matrix = []
        for i,v in enumerate(self.tiles):
            for tile in v.fhr_tile:
                self.match_board(tile, i, matrix)
        return matrix

    def create_matrix_fh(self):
        matrix = []
        for i, v in enumerate(self.tiles):
            for tile in v.fh_tile:
                matrix.append(self.match_board(tile, i, matrix))
        return matrix

    def create_matrix_r(self):
        matrix = []
        for i, v in enumerate(self.tiles):
            for tile in v.r_tile:
                self.match_board(tile, i, matrix)
        return matrix
        # file = open('output.txt', 'r')
        # line = file.readline()
        # while line:
        #     s_l = line.split(',')
        #     matrix.append([int(v) for v in s_l if v != '\n'])
        #     line = file.readline()
        # return matrix


    def create_matrix(self):
        matrix = []
        for i, v in enumerate(self.tiles):
            self.match_board(v.tile, i, matrix)
            # matrix.append(self.match_board(v.tile, i))
        return matrix

    def match_board(self, tile, tile_num, matrix):
        i = 0
        while i <= self.board_length - len(tile):
            j = 0
            while j <= self.board_width - len(tile[0]):
                if self.is_match(self.board.tile ,tile, i, j):
                    line = [0 for _ in range(self.board.area + self.tile_size)]
                    line[self.board.area + tile_num] = 1
                    for k1 in range(0,len(tile)):
                        for k2 in range(0, len(tile[0])):
                            if tile[k1][k2] != ' ':
                                line[self.board.d[(i+k1,j+k2)]] = 1
                    matrix.append(line)
                j+=1
            i+=1

    def is_match(self, board_tile, tile, start_i, start_j):
        # print(tile1)
        # print(tile2)
        for i in range(len(tile)):
            for j in range(len(tile[0])):
                if tile[i][j] != ' ' and tile[i][j] != board_tile[i+start_i][j+start_j]:
                    return False
        return True

    def create_DL(self, matrix):
        Head = Cell(-1,-1)
        cell = Head
        last_cell_of_col = []
        # cell_heads = []
        for i in range(len(matrix[0])):
            cell.set_right(Cell(-1,i))
            cell.right.set_left(cell)
            cell = cell.right
            last_cell_of_col.append(cell)
            self.headers.append(cell)
        cell.right = Head
        Head.left = cell

        for i in range(len(matrix)):
            row_head = Cell(i,-1)
            row_cell = row_head
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    row_cell.set_right(Cell(i,j))
                    row_cell.right.set_left(row_cell)
                    row_cell = row_cell.right
                    row_cell.header = self.headers[j]

                    last_cell_of_col[j].set_down(row_cell)
                    row_cell.set_up(last_cell_of_col[j])
                    last_cell_of_col[j] = row_cell
            row_head = row_head.right
            row_cell.set_right(row_head)
            row_head.set_left(row_cell)
        for i, v in enumerate(self.headers):
            v.set_up(last_cell_of_col[i])
            last_cell_of_col[i].set_down(v)
        return Head
    def dancing1(self, Head):
        head_q = deque()
        head_q.append(Head)
        solutions_q = deque()
        solutions_q.append([])
        tile_set_q = deque()
        tile_set_q.append([])
        recover_q = deque()
        col1 = min(self.headers, key=lambda x: x.count)
        row_q = deque()
        row_q.append(col1.down)
        self.remove(col1)
        q = deque()
        q.append(col1)
        recover_q.append(q)

        solutions = []

        while row_q:
            ans = solutions_q[-1]

            row = row_q[-1]
            if row.row == -1:
                row_q.pop()
                solutions_q.pop()
                tile_set_q.pop()
                self.resume(recover_q.pop())
                if recover_q:
                    self.resume(recover_q.pop())
                continue

            ans_copy = [v for v in ans]
            ans_copy.append(row.row)

            tile_set = tile_set_q[-1]
            shape = self.matrix[row.row][:self.board.area]
            if shape in tile_set:
                row = row.down
                row_q[-1] = row
                continue
            tile_set.append(shape)

            removed_col = deque()
            row_start = row.right
            while row_start.col != row.col:
                # print('remove second:' + str(row_start.header.col))
                self.remove(row_start.header)
                removed_col.append(row_start.header)
                row_start = row_start.right
            recover_q.append(removed_col)

            if Head.right == Head:
                solutions.append(ans_copy)
                t2 = time.time()
                print("It cost %f sec" % (t2 - self.t0))
                self.resume(recover_q.pop())
                row = row.down
                row_q[-1] = row
            else:
                col1 = min(self.headers, key=lambda x: x.count)
                if not col1.count:
                    self.resume(recover_q.pop())
                    row = row.down
                    row_q[-1] = row
                    continue
                else:
                    # print('remove first:' + str(col1.col))
                    self.remove(col1)

                    q = deque()
                    q.append(col1)
                    recover_q.append(q)

                    solutions_q.append(ans_copy)
                    tile_set_q.append([])
                    row_q.append(col1.down)
        return solutions

    def dancing2(self, Head):
        col1 = min(self.headers, key=lambda x:x.count)
        if not col1.count:
            return []
        removed_col = deque()
        tile_set = list()
        # remove first col
        # print('remove first:' + str(col1.col))
        self.remove(col1)
        ans = []
        row = col1.down
        while row.row!=-1:
            # ans.append(row.row)
            shape = self.matrix[row.row][:self.board.area]
            if shape in tile_set:
                row = row.down
                continue
            tile_set.append(shape)

            row_start = row.right
            while row_start.col != row.col:
                # print('remove second:' + str(row_start.header.col))
                self.remove(row_start.header)
                removed_col.append(row_start.header)
                row_start = row_start.right
            if Head.right == Head:
                ans.append([row.row])
                # break
            else:
                ret = self.dancing2(Head)
                if(ret):
                    for v in ret:
                        v.insert(0,row.row)
                        ans.append(v)
                # else:
            self.resume(removed_col)
            row = row.down
        # print()
        q = deque()
        q.append(col1)
        self.resume(q)
        # print(ans)
        return ans


    def remove(self, col):
        if col.col < self.board.area:
            self.headers.remove(col)
        col.left.right = col.right
        col.right.left = col.left

        col = col.down
        while col.row != -1:
            row_start = col.right
            while row_start.col != col.col:
                row_start.header.count -= 1
                # print(str(row_start.header.col) + ' remove  ' + str(row_start.header.count))
                row_start.up.down = row_start.down
                row_start.down.up = row_start.up
                row_start = row_start.right
            col = col.down

    def resume(self, remove_col):
        # self.headers.append(col)
        while remove_col:

            col = remove_col.pop()
            # print('resume:' + str(col.col))

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
            if col.col < self.board.area:
                self.headers.append(col)



if __name__ == '__main__':
    # d = DLX('tests/bad1.txt', flip_h=False, rotate=False)
    d = DLX('testcases/checkerboard.txt', flip_h=True,rotate=True)
    # d = DLX('tests/symmetry5.txt', flip_h=True, rotate=True)
    # d = DLX('testcases/trivial.txt',flip_h= True, rotate=True)

    # read_flie('testcases/trivial.txt')