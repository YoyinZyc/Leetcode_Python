'''
Given HeightMap (matrix)，
starting position, ending position,
输出 从起点到终点的 effort。effort有给定的function ，
可以根据相邻两点高度计 算。

思路：
DP
'''
def calMinEffort(m):
    record = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    for i in range(1,len(m[0])):
        record[0][i] = abs(m[0][i]-m[0][i-1])+record[0][i-1]
    for i in range(1, len(m)):
        record[i][0] = abs(m[i][0]-m[i-1][0])+record[i-1][0]
    for i in range(1,len(m)):
        for j in range(1,len(m[0])):
            record[i][j] = min(abs(m[i][j]-m[i-1][j]) + record[i-1][j], abs(m[i][j]- m[i][j-1])+record[i][j-1])
    print(record)
    return record[-1][-1]
if __name__ == '__main__':
    m = [[2,1,5,7,3],[3,5,1,6,8],[10,23,1,4,9]]
    print(calMinEffort(m))
