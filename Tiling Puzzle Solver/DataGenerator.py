import itertools
from Tile import Tile
class DataGenerator(object):
    def __init__(self, path):
        self.tiles = self.read_flie(path)

    def read_flie(self,path):

        file = open(path,'r')
        lines = []
        line = file.readline()
        tiles_v = []
        tiles_n = []
        lines = []
        while(line):
            lines.append(list(line[:-1]))
            line = file.readline()
        tiles_l = []
        tiles_dict = dict()
        tiles = []
        areas = []
        counts = []
        visited = [[0 for _ in range(len(lines[i]))] for i in range(len(lines))]

        for i, v in enumerate(lines):
            for j, v2 in enumerate(v):
                if v2 != ' ' and not visited[i][j]:
                    cells = []
                    self.create_tile(i,j,lines,cells,visited)
                    zip_cells = list(zip(*list(zip(*cells))[0]))
                    max_i = max(zip_cells[0])
                    min_i = min(zip_cells[0])
                    max_j = max(zip_cells[1])
                    min_j = min(zip_cells[1])
                    width = max_j-min_j+1
                    length = max_i-min_i+1
                    areas.append(width * length)
                    tile = [[' ' for _ in range(width)] for _ in range(length)]
                    for v_c in cells:
                        tile[v_c[0][0]-min_i][v_c[0][1]-min_j] = v_c[1]
                    for k in range(len(tile)):
                        tile[k] = tuple(tile[k])
                    counts.append(len(cells))
                    tile = tuple(tile)
                    # if tile in tiles_l:
                    #     tiles_dict[tile] = tiles_dict.get(tile, set())
                    #     tiles_dict[tile].add(tiles_l.index(tile))
                    #     tiles_dict[tile].add(len(tiles_l))
                    tiles_l.append(tile)

        max_count = max(counts)
        for i, v in enumerate(tiles_l):
            # print(list(v))
            if counts[i] == max_count:
                self.board = Tile(v, counts[i], isBoard=True)
            else:

                tiles.append(Tile(v, counts[i]))



        return tiles

    def create_tile(self, i,j,lines, cells, visited):
        visited[i][j] = 1
        cells.append([(i,j), lines[i][j]])
        # up
        if i-1 >= 0 and j < len(lines[i-1]):
            if not visited[i-1][j] and lines[i-1][j] != ' ':
                self.create_tile(i-1,j,lines,cells,visited)
        # down
        if i+1<len(lines) and j < len(lines[i+1]):
            if not visited[i+1][j] and lines[i+1][j] != ' ':
                self.create_tile(i+1,j,lines,cells,visited)
        # right
        if j -1 >= 0:
            if not visited[i][j-1] and lines[i][j-1] != ' ':
                self.create_tile(i, j-1, lines, cells, visited)
        # left
        if j+1 < len(lines[i]):
            if not visited[i][j+1] and lines[i][j+1] != ' ':
                self.create_tile(i, j+1, lines, cells, visited)


