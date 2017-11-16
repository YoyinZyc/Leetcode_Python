'''
Facebook_Hard
11.06 3:33pm
'''
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [['.' for _ in range(n)] for _ in range(n)]
        return self.helper(board, 0, n)

    def helper(self, board, i, n):
        count = 0
        if i == n:
            # ans.append([''.join(v) for v in board])
            return 1
        for j in range(n):
            if self.check_validate(board, i, j):
                board[i][j] = 'Q'
                count += self.helper(board, i + 1, n)
                board[i][j] = '.'
        return count

    def check_validate(self, board, x, y):
        for i in range(x):
            for j in range(len(board)):
                if board[i][j] == 'Q' and (x + j == i + y or x + y == i + j or y == j):
                    return False
        return True
