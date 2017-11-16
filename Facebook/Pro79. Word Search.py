'''
Facebook_Medium
11.6 6:22pm
'''


# 方法一
def exist(self, board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res

# 方法二
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    record = []
                    if (self.helper(i, j, word[1:], board, record)):
                        return True
        return False

    def helper(self, x, y, word, board, record):
        if not word:
            return True
        record.append([x, y])
        if x > 0 and word[0] == board[x - 1][y] and [x - 1, y] not in record:
            record_copy = [v for v in record]
            if self.helper(x - 1, y, word[1:], board, record_copy):
                return True
        if x < len(board) - 1 and word[0] == board[x + 1][y] and [x + 1, y] not in record:
            record_copy = [v for v in record]
            if self.helper(x + 1, y, word[1:], board, record_copy):
                return True
        if y > 0 and word[0] == board[x][y - 1] and [x, y - 1] not in record:
            print('here')
            record_copy = [v for v in record]
            if self.helper(x, y - 1, word[1:], board, record_copy):
                return True
        if y < len(board[0]) - 1 and word[0] == board[x][y + 1] and [x, y + 1] not in record:
            record_copy = [v for v in record]
            if self.helper(x, y + 1, word[1:], board, record_copy):
                return True
        return False

