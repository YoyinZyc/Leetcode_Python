'''
给一个matrix，要求找到从左上角到右下角，字典序排序最小的一条路径

思路：
dfs+greedy
时间复杂度 N!
'''
def path(matrix):
    l = len(matrix) + len(matrix[0]) - 2
    def helper(path, loc, val, l):
        # 到达终点
        if loc[0] == len(matrix)-1 and loc[1] == len(matrix[0])-1:
            return (val, path + [matrix[loc[0]][loc[1]]])
        # 必须向右
        if loc[0]+1 == len(matrix):
            return helper(path+ [matrix[loc[0]][loc[1]]], [loc[0], loc[1]+1], val + (ord(matrix[loc[0]][loc[1]]) - ord('a'))* (26 ** l), l-1)
        # 必须向下
        if loc[1]+1 == len(matrix[0]):
            return helper(path + [matrix[loc[0]][loc[1]]], [loc[0]+1, loc[1]],
                          val + (ord(matrix[loc[0]][loc[1]]) - ord('a')) * (26 ** l), l - 1)
        # 判断向右向下
        if ord(matrix[loc[0]+1][loc[1]]) > ord(matrix[loc[0]][loc[1]+1]):
            return helper(path + [matrix[loc[0]][loc[1]]], [loc[0], loc[1] + 1],
                          val + (ord(matrix[loc[0]][loc[1]]) - ord('a')) * (26 ** l), l - 1)
        elif ord(matrix[loc[0]+1][loc[1]]) < ord(matrix[loc[0]][loc[1]+1]):
            return helper(path + [matrix[loc[0]][loc[1]]], [loc[0] + 1, loc[1]],
                          val + (ord(matrix[loc[0]][loc[1]]) - ord('a')) * (26 ** l), l - 1)
        # 如果右边和下边的字母相同，dfs
        else:
            down = helper(path + [matrix[loc[0]][loc[1]]], [loc[0] + 1, loc[1]],
                          val + (ord(matrix[loc[0]][loc[1]]) - ord('a')) * (26 ** l), l - 1)
            right = helper(path + [matrix[loc[0]][loc[1]]], [loc[0], loc[1] + 1],
                          val + (ord(matrix[loc[0]][loc[1]]) - ord('a')) * (26 ** l), l - 1)
            if down[0] > right[0]:
                return right
            return down
    return helper([], [0,0], 0, l)
if __name__ == '__main__':
    matrix = [['a','c','d','e','f'], ['c','c','h','a','a'], ['w','a','z','z','z']]
    print(path(matrix))