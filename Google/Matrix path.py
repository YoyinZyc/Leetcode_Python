'''
给一个二维格子，给出start location 和 end location，有一 些格子是blocked
或者 open的 ，请找出一条path能够从start 到end。。。只找出一条即可

BFS
O(NM*4^k)
'''
def matrix_path(start, end, matrix):
    visited = []
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    def helper(path, loc):
        if loc == end:
            return path
        if loc in visited or matrix[loc[0]][loc[1]] or loc[0] < 0 or loc[0] >= len(matrix) or loc[1] < 0 or loc[1] >= len(matrix[0]):
            return []
        visited.append(loc)
        for v in dirs:
            ret = helper(path+[loc], [loc[0]+v[0], loc[1]+v[1]])
            if ret:
                return ret
    return helper([], start)
