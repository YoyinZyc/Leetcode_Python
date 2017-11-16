'''
Facebook_Hard
11.06 3:20pm
'''
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.helper(board, 0, ans, n)
        return ans
    def helper(self,board, i, ans, n):
        if i == n:
            ans.append([''.join(v) for v in board])
        for j in range(n):
            if self.check_validate(board, i, j):
                board[i][j] = 'Q'
                self.helper(board, i+1, ans, n)
                board[i][j] = '.'
    def check_validate(self,board, x, y):
        for i in range(x):
            for j in range(len(board)):
                if board[i][j] == 'Q' and (x+j == i+y or x+y == i+j or y == j):
                    return False
        return True