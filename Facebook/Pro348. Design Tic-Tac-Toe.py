'''
Facebook_Medium
11.8 9:30pm
'''


# 方法一：O(1)
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0 for _ in range(n)]
        self.col = [0 for _ in range(n)]
        self.n = n
        self.diagonal = 0
        self.anti_d = 0
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        add = -1
        if player == 1:
            add = 1
        self.row[row] += add
        self.col[col] += add
        if row == col:
            self.diagonal += add
        if row + col == self.n-1:
            self.anti_d += add
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_d) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# 方法2 O(n)
class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.has_win = False
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if not self.has_win:
            if row < 0 or col < 0 or row >= self.n or col >= self.n:
                return 0
            # print(self.board)
            if self.board[row][col]:
                return 0
            self.board[row][col] = player
            i = 0

            while i < self.n and self.board[row][i] == player:
                i += 1
            if i == self.n:
                return player
            i = 0
            while i < self.n and self.board[i][col] == player:
                i += 1
            if i == self.n:
                return player

            if row == col:
                i = 0
                while i < self.n and self.board[i][i] == player:
                    i += 1
                if i == self.n:
                    return player
            if col + row == self.n - 1:
                i = 0
                while i < self.n and self.board[i][self.n - i - 1] == player:
                    i += 1
                if i == self.n:
                    return player
            return 0



            # Your TicTacToe object will be instantiated and called as such:
            # obj = TicTacToe(n)
            # param_1 = obj.move(row,col,player)