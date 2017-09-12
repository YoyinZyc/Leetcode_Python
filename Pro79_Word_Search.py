'''
Backtracking_Medium
9.11 7:35pm
'''
import copy
class installpySolution(object):
	"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
	"""
	def exist(self, board, word):
		firstLine = [1] * (len(board[0])+2);
		otherLine = [[1] + [0]*len(board[0]) + [1]]
		indexBoard = [firstLine]
		for i in range(len(board)):
			indexBoard.append([[1] + [0]*len(board[0]) + [1]]) 
		# print (otherLine)
		indexBoard += [firstLine]
		# print (indexBoard)
		for i in range(len(board)):
			for j in range(len(board[0])):
				if(board[i][j] == word[0]):
				
					indexBoardClone = copy.deepcopy(indexBoard)
					print(indexBoardClone[i+1][j+1])

					indexBoardClone[i+1][j+1] = 1
					print(indexBoardClone)
					if(self.helper(board, indexBoardClone, word, 1, i, j)):
						return True
		return False
	   
	def helper(self, board, indexBoard, word, index, i, j):
		print(indexBoard)
		if(index == len(word)): 
			return True
		if(indexBoard[i][j+1] != 1 and word[index] == board[i-1][j]):
			print('top')
			indexBoardClone = copy.deepcopy(indexBoard)
			indexBoardClone[i][j+1] = 1
			if(self.helper(board, indexBoardClone, word, index+1, i-1, j)):
				return True
		if(indexBoard[i+2][j+1] != 1 and word[index] == board[i+1][j]):
			print('bottom')
			indexBoardClone = copy.deepcopy(indexBoard)
			indexBoardClone[i+2][j+1] = 1
			if(self.helper(board, indexBoardClone, word, index+1, i+1, j)):
				return True
		if(indexBoard[i+1][j] != 1 and word[index] == board[i][j-1]):
			print('left')
			indexBoardClone = copy.deepcopy(indexBoard)
			indexBoardClone[i+1][j] = 1
			if(self.helper(board, indexBoardClone, word, index+1, i, j-1)):
				return True
		if(indexBoard[i+1][j+2] != 1 and word[index] == board[i][j+1]):
			print('right')
			indexBoardClone = copy.deepcopy(indexBoard)
			indexBoardClone[i+1][j+2] = 1
			if(self.helper(board, indexBoardClone, word, index+1, i, j+1)):
				return True
		
		return False;  

	# def exist(self, board, word):
 #        if not board:
 #            return False
 #        for i in xrange(len(board)):
 #            for j in xrange(len(board[0])):
 #                if self.dfs(board, i, j, word):
 #                    return True
 #        return False

 #    def dfs(self, board, i, j, word):
	# 	if len(word) == 0: # all the characters are checked
 #        	return True
	# 	if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
 #        	return False
 #        tmp = board[i][j]  # first character is found, check the remaining part
 #        board[i][j] = "#"  # avoid visit agian 
   
 #        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
 #        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
 #        board[i][j] = tmp
 #        return res        





