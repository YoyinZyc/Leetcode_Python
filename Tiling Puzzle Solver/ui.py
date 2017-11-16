import sys
import random
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QHBoxLayout,QVBoxLayout,QLabel,QCheckBox, QLineEdit, QFrame, QFileDialog)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

from DLX import DLX
from Tile import Tile
from collections import deque

class Square(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # self.update()
    def drawSquare(self, painter, x, y, shape):
        color = QColor(random.randint(0,225), random.randint(0,225), random.randint(0,225))
        painter.fillRect(10,10,20,20,color)

        painter.setPen(color.lighter())
        # painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        # painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        # painter.drawLine(x + 1, y + self.squareHeight() - 1,
        #                  x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        # painter.drawLine(x + self.squareWidth() - 1,
        #                  y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

    # def paintEvent(self, e):
    #     qp = QPainter()
    #     qp.begin(self)
    #     self.drawRectangles(qp)
    #     qp.end()
    #
    # def drawRectangles(self, qp):
    #     col = QColor(0, 0, 0)
    #     col.setNamedColor('#d4d4d4')
    #     qp.setPen(col)
    #
    #     qp.setBrush(QColor(200, 0, 0))
    #     qp.drawRect(10, 15, 90, 60)
    #
    #     qp.setBrush(QColor(255, 80, 0, 160))
    #     qp.drawRect(130, 15, 90, 60)
    #
    #     qp.setBrush(QColor(25, 0, 90, 200))
    #     qp.drawRect(250, 15, 90, 60)
    def paintEvent(self, event):
        painter = QPainter(self)
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        color = QColor(random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))
        painter.setPen(color)
        # painter.setBrush(QColor(100,0,0))
        # painter.drawRect(10,10,10,10)
        # color = QColor(random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))
        painter.fillRect(40, 40, 40, 40, color)

        # painter.setPen(color.lighter())
        # painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        # painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        # painter.setPen(color.darker())
class Board(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("QWidget { background-color: white}")
    # def show_board(self, board):
    #
    # def show_solution(self, tiles, solution):


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.rotate_status = False
        self.ref_status = False
        self.count = 0
        self.len_solution = 0
        self.initUI()
        self.grids = []
    def initUI(self):


        display = QVBoxLayout()
        file_name = QHBoxLayout()
        file_name.addWidget(QLabel('File name:'))
        # self.name_label = QLabel()
        self.name_label = QLineEdit()
        self.name_label.setReadOnly(True)
        file_name.addWidget(self.name_label)
        # file_name.addWidget(self.name_label)

        self.board = Board(self)
        # self.test()
        # self.label = QLabel(self.board)
        # self.label.setStyleSheet("QWidget { background-color: red; border:2px solid grey}")
        # self.label.setGeometry(20, 20, 40, 40)
        #

        # grid.setGeometry(150,20,100,100)
        # grid.setStyleSheet("QWidget { background-color: white}")
        # print(grid.width())
        # print(grid.height())
        # self.square.setGeometry(150, 20, 100, 100)
        # self.square.setStyleSheet("QWidget { background-color: %s }" %
        #                           self.col.name())
        # grid = QGridLayout()
        # grid.setSpacing(0)
        # print(self.contentsRect().width())
        # self.setLayout(grid)

        # names = ['Cls', 'Bck', '', 'Close',
        #          '7', '8', '9', '/',
        #          '4', '5', '6', '*',
        #          '1', '2', '3', '-',
        #          '0', '.', '=', '+']
        #
        # positions = [(i, j) for i in range(5) for j in range(4)]
        # print(positions)
        # for position, name in zip(positions, names):
        #
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position)
        # grid_layout = QGridLayout()
        # for i in range(10):
        #     grid_layout.addWidget(Square(), 0, i,1,1)


        # rec1 = Square(self)

        # rec1.move(30,30)
        # rec1.setGeometry(20,20,40,40)
        # rec1.show()
        # grid_layout.add
        # rec1.show()
        # rec2 = Square()
        #
        # gird_layout.addWidget(rec1,0,0)
        # gird_layout.addWidget(rec2, 1, 0)
        # grid.setLayout(grid_layout)
        # grid.addWidget(rec2,0,1)



        result = QHBoxLayout()
        self.count_label = QLabel('0/0')
        result.addWidget(self.count_label)

        self.prev_solution = QPushButton('Prev')
        self.prev_solution.clicked.connect(self.show_prev_solution)
        result.addWidget(self.prev_solution)

        self.next_solution = QPushButton('Next')
        self.next_solution.clicked.connect(self.show_next_solution)
        result.addWidget(self.next_solution)



        display.addLayout(file_name)
        display.addWidget(self.board)
        display.addLayout(result)
        control = QVBoxLayout()
        open_button = QPushButton('Open File')
        open_button.clicked.connect(self.openFileNameDialog)
        control.addWidget(open_button)

        rotate = QCheckBox('rotate')
        rotate.stateChanged.connect(self.changeRotateStatus)
        control.addWidget(rotate)

        reflect = QCheckBox('reflect')
        reflect.stateChanged.connect(self.changeRefStatus)
        control.addWidget(reflect)

        show_solutions = QPushButton('Show Solutions')
        show_solutions.clicked.connect(self.getSolutions)
        control.addWidget(show_solutions)

        layout = QHBoxLayout()

        layout.addLayout(display)
        layout.addLayout(control)
        # author = QLabel('Author')

        # layout.addWidget(author)
        layout.setSpacing(20)
        self.setLayout(layout)

        self.resize(800,600)


        # print(self.name_label.text() == "")


        self.move(300, 150)
        self.setWindowTitle('Tiling Solver')
        self.show()
    def test(self):
        label2 = QLabel(self.board)
        label2.setStyleSheet("QWidget { background-color: black}")
        label2.setGeometry(540, 410, 40, 40)
        label2.show()
        # label2.update()
        # self.update()

    def openFileNameDialog(self):


        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.name_label.setText(fileName)
            self.name_label.update()
            self.count_label.setText('0/0')
            return fileName
    def getSolutions(self):
        # label2 = QLabel(self.board)
        # label2.setStyleSheet("QWidget { background-color: black}")
        # label2.setGeometry(540, 410, 40, 40)
        # self.update()
        path = self.name_label.text()
        print(1)
        if path != "":
            dlx = DLX(path, rotate=self.rotate_status, flip_h=self.ref_status)
            self.solutions = dlx.solutions

            # print(self.solutions)
            self.matrix = dlx.matrix
            self.init_board(dlx.board.tile)
            self.board_area = dlx.board.area
            self.d_r = dlx.board.d_r
            self.colors = self.generate_color(dlx.tile_size)

            if self.solutions:
                self.next_solution.setEnabled(True)
                self.prev_solution.setEnabled(False)
                self.solution_q = deque(self.solutions)
                self.count = 0
                self.len_solution = len(self.solutions)
                self.show_next_solution()



            else:
                self.next_solution.setEnabled(False)
    def generate_color(self, tile_num):
        colors = []
        for _ in range(tile_num):
            rand_r = random.randint(0,224)
            rand_g = random.randint(0,224)
            rand_b = random.randint(0,224)
            colors.append(QColor(rand_r, rand_g, rand_b))
        return colors
    def show_next_solution(self):
        self.count+=1
        self.count_label.setText(str(self.count) + '/' + str(self.len_solution))
        sol = self.solutions[self.count-1]
        # self.solution_q.insert(0,sol)
        for row in sol:
            line = self.matrix[row]
            i = 0
            index = line[self.board_area:].index(1)
            while i < self.board_area:
                if line[i]:
                    # x = i // len(self.grids[0])
                    # y = i % len(self.grids[0])
                    (x,y) = self.d_r[i]
                    self.grids[x][y].setStyleSheet("QWidget {background-color: %s; border:1px solid grey}" %self.colors[index].name())
                i+=1
        if self.count == self.len_solution:
            self.next_solution.setEnabled(False)
        if self.count > 1:
            self.prev_solution.setEnabled(True)
    def show_prev_solution(self):
        self.count-=1
        self.count_label.setText(str(self.count) + '/' + str(self.len_solution))
        # sol = self.solution_q.popleft()
        # self.solution_q.append(sol)
        sol = self.solutions[self.count - 1]
        for row in sol:
            line = self.matrix[row]
            i = 0
            index = line[self.board_area:].index(1)
            while i < self.board_area:
                if line[i]:
                    # x = i // len(self.grids[0])
                    # y = i % len(self.grids[0])
                    (x,y) = self.d_r[i]
                    self.grids[x][y].setStyleSheet("QWidget {background-color: %s; border:1px solid grey}" %self.colors[index].name())
                i+=1
        if self.count == 1:
            self.prev_solution.setEnabled(False)
        if self.count < self.len_solution:
            self.next_solution.setEnabled(True)


            # if not self.solutions:

    def init_board(self, board_tile):
        # label2 = QLabel(self.board)
        # label2.setStyleSheet("QWidget { background-color: black}")
        # label2.setGeometry(540, 410, 40, 40)
        if self.grids:
            for i in self.grids:
                for j in i:
                    j.setParent(None)
            self.grids = []
        width = len(board_tile[0])
        length = len(board_tile)

        border_len = int(min(560/width, 430/length))
        start_x = int(560 / 2 - border_len * (width/2) + 20)
        start_y = int(430 / 2 - border_len * (length / 2) + 20)

        content_set = set()
        for i in range(length):
            line = []
            for j in range(width):
                label = QLabel(self.board)

                label.setStyleSheet("QWidget {border:1px solid grey}")
                label.setGeometry(start_x + border_len*j, start_y + border_len*i, border_len, border_len)
                line.append(label)
                if board_tile[i][j] != ' ':
                    content_set.add(board_tile[i][j])
            self.grids.append(line)
        if len(content_set) > 1:
            for i in range(length):
                for j in range(width):
                    if board_tile[i][j] != ' ':
                        self.grids[i][j].setText(board_tile[i][j])
        for i in range(length):
            for j in range(width):
                self.grids[i][j].show()





    def changeRotateStatus(self, state):
        if state == Qt.Checked:
            self.rotate_status = True
        else:
            self.rotate_status = False
    def changeRefStatus(self, state):
        if state == Qt.Checked:
            self.ref_status = True
        else:
            self.ref_status = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())