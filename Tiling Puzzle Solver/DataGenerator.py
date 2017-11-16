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
            # if line != '\n':
            lines.append(list(line[:-1]))
            line = file.readline()
        tiles_l = []
        tiles_dict = dict()
        tiles = []
        areas = []
        counts = []
        visited = [[0 for _ in range(len(lines[i]))] for i in range(len(lines))]
        # print(len(visited[0]))
        # print(len(lines[0]))
        # print(lines)

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
                # if v in tiles_dict
                # if v in tiles_dict:
                # tiles_dict[v].remove(i)
                # if v not in tiles_l[:i]:
                tiles.append(Tile(v, counts[i]))
                # else:
                #     j = i-1
                #     while j >= 0:
                #         if tiles_l[j] == v:
                #             dup = [d for d in tiles[j].dup]
                #             dup.append(j)
                #             tiles.append(Tile(v, counts[i], dup))
                #             break
                #         j-=1
                    # tiles_dict[v].add(i)


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

        # width = 0
        # lastwidth = len(lines[start_i])
        # tile = []
        # i = start_i
        # # temp = lines[i][start_j]
        # while i < len(lines) and start_j < len(lines[i]):
        #     j = start_j
        #     has_value = False
        #     while j < len(lines[i]):
        #         if lines[i][j] != ' ':
        #             visited[i][j] = 1
        #             has_value = True
        #         else:
        #             if i == start_i:
        #                 break
        #             else:
        #                 if j >= lastwidth:
        #                     break
        #
        #         j+=1
        #     if has_value:
        #         width = max(width, j-start_j)
        #         lastwidth = j-1
        #         i+=1
        #     else:
        #         break
        #     # tile.append(lines[i][j:k])
        # while start_i < i:
        #     l = lines[start_i][start_j:start_j+width]
        #     if len(l) < width:
        #         l = l + [' ' for _ in range(width-len(l))]
        #     tile.append(l)
        #     start_i+=1
        # tiles_l.append(tuple(tile))
        # areas.append(len(tile) * len(tile[0]))
        # print(lines)
        # columns = [list(filter(None, pair)) for pair in itertools.zip_longest(*lines)]
        # print(columns)
        #
        # i = 0
        # while i < len(columns):
        #
        #     if columns[i].count(' ') != len(columns[i]):
        #         j = i
        #         while i < len(columns) and columns[i].count(' ') != len(columns[i]):
        #             i+=1
        #         tile = tuple(zip(*columns[j:i]))
        #         tiles_l.append(tile)
        #         areas.append(len(tile) * len(tile[0]))
        #     i+=1


