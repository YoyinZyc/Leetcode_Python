'''
Microsoft_Medium
10.31 10:11pm
'''
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if self.isLeft(i, j, board) and self.isTop(i, j, board):
                        count += 1
        return count

    def isLeft(self, i, j, board):
        if j == 0:
            return True
        return board[i][j - 1] == '.'

    def isTop(self, i, j, board):
        if i == 0:
            return True
        return board[i - 1][j] == '.'
