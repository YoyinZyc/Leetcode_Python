'''
BFS_Medium
9.15 11:48am
'''


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # firstLine = [1 for col in range(len(heightMap[0]))]
        # lastLine = [1 for col in range(len(heightMap[0]))]
        # visited = [[1]+[0 for col in range(len(heightMap[0]-2))]+[1] for row in range(len(heightMap)-2)]
        # visited = [firstLine] + visited + [lastLine]
        d = dict()
        for i in range(1, len(heightMap)-1):
            for j in range(1, len(heightMap[0])-1):
                if j -1 == 0:
                    d.setdefault((i,j),[]).append(heightMap[i][0])
                else:
                    d.setdefault((i,j),[]).append(max(d[(i,j-1)],heightMap[i][j-1]))
                if i -1 == 0:
                    d.setdefault((i,j),[]).append(heightMap[0][j])
                else:
                    d.setdefault((i, j), []).append(max(d[(i-1, j)], heightMap[i-1][j]))
        for i in range(1, len(heightMap)-1):
            for j in range(1, len(heightMap[0])-1):
                if j -1 == 0:
                    d.setdefault((i,-1-j),[]).append(heightMap[i][-1])
                else:
                    d.setdefault((i,-1-j),[]).append(max(d[(i,-j)],heightMap[i][-j]))
                if i -1 == 0:
                    d.setdefault((-1-i,j),[]).append(heightMap[-1][j])
                else:
                    d.setdefault((-1-i, j), []).append(max(d[(-i, j)], heightMap[-i][j]))

        area = sum(v-heightMap[k[0]][k[1]] for k,v in d if v > heightMap[k[0]][k[1]])
        return  area


