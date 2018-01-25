'''
Game of board这个游戏

思路:
利用位运算,四种情况
0->1：10
0->0：00
1->1：11
1->0：01
判断neighbor的时候和1做与运算
最后把所有值都右移一位

follow up：
1 这个board能上下连起来，也 可以左右连起来，如何找到下 一阶段的状态。 连起来问题就是对边界取模

2 board太大，可以多台机器处 理，那么如何切割board，对于 切割的一小块，有什么需要注 意的，如何解决。
2.切割出来的小board要注意 边界问题，解决办法就是在 他们外面再加一圈。然后切 割的办法，
我先提出常规的 按行和按列切割，然后面试 官说你这样切割，一个 machine就会有八个邻居，跟 八个邻居交流会很花时间，
如何解决?然后给了一个列 子提示了一下，我就想到可 以把多行弄成一行，
然后二 分切割，这样一个机器就只 会有左右两个邻居。多重信 息
'''
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def countLive(x,y):
            count = 0
            for i in range(max(x-1,0),min(len(board), x+2)):
                for j in range(max(y-1,0), min(len(board[0]), y+2)):
                    # 判断neighbor的时候和1做与运算
                    if (i!=x or j != y) and board[i][j] & 1:
                        count += 1
            return count
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = countLive(i,j)
                if board[i][j]:
                    if count >= 2 and count <= 3:
                        board[i][j] = 3
                else:
                    if count == 3:
                        board[i][j] = 2
        # 最后把所有值都右移一位
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] >> 1